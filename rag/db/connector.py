import os
from dotenv import load_dotenv 
import json
from sqlalchemy import create_engine, URL
from llama_index.core.chat_engine.types import ChatMode
from llama_index.core import Document, StorageContext, VectorStoreIndex, Settings
from llama_index.vector_stores.tidbvector import TiDBVectorStore
from llama_index.embeddings.gemini import GeminiEmbedding
from llama_index.llms.groq import Groq
from llama_index.core.vector_stores import MetadataFilter, MetadataFilters
from datetime import datetime
from enums.country import Country
from models.chat_message import ChatMessages
from third_parties.weather import (
    get_weather_data, 
    get_weather_calculation,
    summarize_weather_data,
)

load_dotenv() 

# Tidb connection URL
tidb_connection_url = URL.create(
    drivername="mysql+pymysql",
    username=os.getenv('TIDB_USERNAME'),
    password=os.getenv('TIDB_PASSWORD'),
    host=os.getenv('TIDB_HOST'),
    port=4000,
    database="test",
    query={"ssl_verify_cert": "false", "ssl_verify_identity": "true"},
)

# Create an engine
engine = create_engine(tidb_connection_url, pool_recycle=3600)

# TiDB Vector Store
tidbvec = TiDBVectorStore(
    connection_string=tidb_connection_url,
    table_name=os.getenv("VECTOR_TABLE_NAME"),
    distance_strategy="cosine",
    vector_dimension=768,
    drop_existing_table=False,
)

# Storage context
storage_context = StorageContext.from_defaults(vector_store=tidbvec)

# Preprocess data
def preprocess_data(path):
    documents = []
    with open(path, "r") as file:
        data = json.load(file)
        for item in data:
            text = f"""
            Address: {item['address']}
            Title: {item['title']}
            Country: {item['complete_address']['country']}
            Categories: {', '.join(item.get('categories', []))}
            Description: {item.get('description', 'No description')}
            Review Count: {item['review_count']}
            Review Rating: {item['review_rating']}
            Open Hours: {json.dumps(item['open_hours'])}
            Latitude: {item['latitude']}
            Longitude: {item['longtitude']}
            """
            metadata = {
                "id": item["cid"],
                "title": item["title"],
                "description": item["description"],
                "address": item["address"],
                "complete_address": item["complete_address"],
            }
            document = Document(text=text, metadata=metadata)
            documents.append(document)
    return documents

# Initialize the vector store index
def init():
    documents = preprocess_data("./data/destinations.json")
    index = VectorStoreIndex.from_documents(
        documents, storage_context=storage_context, insert_batch_size=1000, show_progress=True
    )
    return index

# Connect to the vector store
def connect():
    index = VectorStoreIndex.from_vector_store(vector_store=tidbvec)
    return index

# Settings for the LLM and embedding model
Settings.llm = Groq(model="llama3-70b-8192", api_key=os.getenv("GROQ_API_KEY"))
Settings.embed_model = GeminiEmbedding(api_key=os.getenv("GEMINI_API_KEY"))

# Connect to the index
index = connect()

# Get destination by CID
def get_destination_by_cid(cid):
    with open("./data/destinations.json", "r") as file:
        data = json.load(file)
        for item in data:
            if item["cid"] == cid:
                return item
    return None

# Get data from CIDs
def get_data_from_cids(cids):
    with open("./data/destinations.json", "r") as file:
        data = json.load(file)
        results = []
        for cid in cids:
            for item in data:
                if item["cid"] == cid:
                    results.append(item)
    return results

# Query handler
def query(
    date: str,
    country: Country,
    startTime: str,
    endTime: str,
    address: str,
    lat: float,
    lng: float,
):
    return query_retry_handler(date, country, startTime, endTime, address, lat, lng)

# Retry handler for query
def query_retry_handler(
    date: str,
    country: Country,
    startTime: str,
    endTime: str,
    address: str,
    lat: float,
    lng: float,
    retry=0,
):
    try:
        filters = MetadataFilters(
            filters=[
                MetadataFilter(
                    key="complete_address.country",
                    value=[country.value],
                )
            ]
        )
        
        weather_data = get_weather_data(lat, lng, date, startTime, endTime)
        weather_calculation = get_weather_calculation(weather_data)
        weather_prompt = summarize_weather_data(weather_calculation)

        query_engine = index.as_query_engine(
            filters=filters,
            similarity_top_k=2,
        )
        response = query_engine.query(
            create_prompt(date, startTime, endTime, address, weather_prompt)
        )
        metadata_ids = [value["id"] for value in response.metadata.values()]
        source_node_ids = [node.node.metadata["id"] for node in response.source_nodes]

        print(metadata_ids)
        print(source_node_ids)

        return {
            "response": response.response,
            "metadata": get_data_from_cids(list(set(metadata_ids + source_node_ids))),
            "weathers": weather_data,
            "weather_calculation": weather_calculation,
        }
    except Exception as e:
        if retry < 3:
            print(f"Retrying {retry}...")
            return query_retry_handler(date, country, startTime, endTime, address, lat, lng, retry + 1)
        else:
            print(e)
            return {
                "response": "An error occurred. Please try again later.",
                "error": str(e)
            }

# Chat query handler
def chat_query(
    messages: ChatMessages,
    query: str,
    day: str,
    country: Country,
    startTime: str,
    endTime: str,
    address: str,
):
    filters = MetadataFilters(
        filters=[
            MetadataFilter(
                key="complete_address.country",
                value=[country.value],
            )
        ]
    )
    
    histories = [
        ChatMessage(content=message.content, role=message.role, additional_kwargs={})
        for message in messages.histories
    ]
    
    histories.insert(0, ChatMessage(
        content=(
            f"You are a travel itinerary planner. Create a memorable and engaging sightseeing itinerary for "
            f"visitors to {address} on {day}. The itinerary should cover the time range from {startTime} to {endTime}. "
            "Ensure that the itinerary is well-paced, with time allocated for each activity, including travel time "
            "between locations. The itinerary should cater to a leisurely and enjoyable experience, including suggestions "
            "for dining, leisure, and unique sightseeing spots. Please ensure that the venues are open during the specified "
            "time range and that the itinerary is feasible. Do not include any locations, activities, or suggestions that are "
            "not present in the provided data. The itinerary must include at least three distinct destinations."
        ),
        role="system",
        additional_kwargs={},
    ))
    
    histories.append(ChatMessage(content=query, role="user", additional_kwargs={}))
    
    query_engine = index.as_chat_engine(
        filters=filters,
        chat_mode=ChatMode.CONTEXT, 
        llm=Settings.llm, 
        verbose=True,
    )
    response = query_engine.chat(query, chat_history=histories)
    source_node_ids = [node.node.metadata["id"] for node in response.source_nodes]

    print(source_node_ids)
   
    return {
        "response": response.response,
        "metadata": get_data_from_cids(source_node_ids),
    }

# Retry handler for chat queries
def chat_retry_handler(
    messages: ChatMessages,
    query: str,
    day: str,
    country: Country,
    startTime: str,
    endTime: str,
    address: str,
    retry=0,
):
    try:
        return chat_query(messages, query, day, country, startTime, endTime, address)
    except Exception as e:
        if retry < 3:
            print(f"Retrying {retry}...")
            return chat_retry_handler(messages, query, day, country, startTime, endTime, address, retry + 1)
        else:
            print(e)
            return {
                "response": "An error occurred. Please try again later.",
                "error": str(e)
            }

# Prompt creation
def create_prompt(
    date: str,
    startTime: str,
    endTime: str,
    address: str,
    weather_summary: str,
):
    day = format_date(date, "%A")
    prompt = (
        f"You are a travel itinerary planner. Create a memorable and engaging sightseeing itinerary for "
        f"visitors to {address} on {day}. The itinerary should cover the time range from {startTime} to {endTime}. "
        "Ensure that the itinerary is well-paced, with time allocated for each activity, including travel time "
        "between locations. The itinerary should cater to a leisurely and enjoyable experience, including suggestions "
        "for dining, leisure, and unique sightseeing spots. Please ensure that the venues are open during the specified "
        "time range and that the itinerary is feasible. "
    )

    if weather_summary:
        prompt += f"Consider the following summarized weather data when planning the itinerary: {weather_summary}. "

    prompt += (
        "Do not include any locations, activities, or suggestions that are not present in the provided data. "
        "The itinerary must include at least three distinct destinations."
    )
    return prompt.strip()

# Format date
def format_date(date_str, format_str):
    return datetime.strptime(date_str, "%Y-%m-%d").strftime(format_str)
