Installation
Clone the repository:

git clone https://github.com/priyansh2120/cursed-apple.git
cd cursed-apple
# read the README.md
Set up the LLM:

Navigate to the llm directory and install Python dependencies:
cd rag
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt

create the .env
Set up the Server:

Navigate to the server directory and install Node.js dependencies:
cd ../server
npm install

Set up the Client:

Navigate to the client directory and install Node.js dependencies:
cd ../client
npm install

Set up environment variables:

Create a .env file in each of the llm, server, and client directories using the provided templates.
Usage
Running the LLM
To start the LLM service:

cd llm
python main.py
Running the Server
To start the FastAPI and Node.js servers:

cd server
npm run start
Running the Client
To start the client application:

cd client
npm run dev
