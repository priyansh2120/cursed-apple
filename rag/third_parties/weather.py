import os
import requests

def get_weather_data(
    lat: float,
    lng: float,
    date: str,
    startTime: str,
    endTime: str,
):
    try:
        response = requests.get(f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{lat},{lng}/{date}?key={os.getenv('VISUAL_CROSSING_API_KEY')}")
        response.raise_for_status()
        data = response.json()
        
        print(f"Weather API response: {data}")
        
        if "days" not in data or not data["days"]:
            print("Warning: No 'days' data in the weather API response")
            return []
        
        day_data = data["days"][0]
        
        # Create a single weather data point for the entire day
        weather_data = {
            "date": day_data.get("datetime", ""),
            "temp": day_data.get("temp", None),
            "feelslike": day_data.get("feelslike", None),
            "precipprob": day_data.get("precipprob", None),
            "conditions": day_data.get("conditions", ""),
            "cloudcover": day_data.get("cloudcover", None),
            "uvindex": day_data.get("uvindex", None),
        }
        
        return [weather_data]
    except Exception as e:
        print(f"Error fetching weather data: {e}")
        return []
    

def get_weather_calculation(weather_data_list):
    if not weather_data_list:
        return None

    avg_temp = sum(item['temp'] for item in weather_data_list) / len(weather_data_list)
    avg_feelslike = sum(item['feelslike'] for item in weather_data_list) / len(weather_data_list)
    avg_precipprob = sum(item['precipprob'] for item in weather_data_list) / len(weather_data_list)
    max_precipprob = max(item['precipprob'] for item in weather_data_list)
    predominant_conditions = max(set(item['conditions'] for item in weather_data_list), key=lambda c: sum(1 for item in weather_data_list if item['conditions'] == c))
    avg_cloudcover = sum(item['cloudcover'] for item in weather_data_list) / len(weather_data_list)
    max_uvindex = max(item['uvindex'] for item in weather_data_list)

    return {
        "avg_temp": avg_temp,
        "avg_feelslike": avg_feelslike,
        "avg_precipprob": avg_precipprob,
        "max_precipprob": max_precipprob,
        "predominant_conditions": predominant_conditions,
        "avg_cloudcover": avg_cloudcover,
        "max_uvindex": max_uvindex,
    }

def summarize_weather_data(calculation):
    if not calculation:
        return None
    
    weather_summary = f"Average temperature: {calculation['avg_temp']:.1f}°F (feels like {calculation['avg_feelslike']:.1f}°F). "
    weather_summary += f"Average precipitation probability: {calculation['avg_precipprob']:.1f}%, with a maximum of {calculation['max_precipprob']}%. "
    weather_summary += f"Predominant conditions: {calculation['predominant_conditions']}. "
    weather_summary += f"Average cloud cover: {calculation['avg_cloudcover']:.1f}%. "
    weather_summary += f"Maximum UV index: {calculation['max_uvindex']}."

    return weather_summary