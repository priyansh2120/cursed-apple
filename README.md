# Cursed Apple

This repository contains the full stack for the **Cursed Apple** project, including the LLM, server, and client components.

## Installation

### Clone the repository:
```bash
git clone https://github.com/priyansh2120/cursed-apple.git
cd cursed-apple
```

### Set up the LLM:

1. Navigate to the LLM directory:
   ```bash
   cd rag
   ```

2. Set up a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```



### Set up the Server:

1. Navigate to the server directory:
   ```bash
   cd ../backend
   ```

2. Install Node.js dependencies:
   ```bash
   npm install
   ```

3. Create a `.env` file inside the `backend` directory using the provided template.

### Set up the Client:

1. Navigate to the client directory:
   ```bash
   cd ../frontend
   ```

2. Install Node.js dependencies:
   ```bash
   npm install
   ```

3. Create a `.env` file inside the `frontend` directory using the provided template.

---

## Usage

### Running the LLM

1. To start the LLM service:
   ```bash
   cd rag
   fastapi run main.py
   ```

### Running the Server

1. Navigate to the server directory:
   ```bash
   cd backend
   ```

2. Run the server ( Node.js):
   ```bash
   npm run start
   ```

### Running the Client

1. Navigate to the client directory:
   ```bash
   cd frontend
   ```

2. Start the client application:
   ```bash
   npm run dev
   ```

---


## How to run the app locally

1. Clone the repository and navigate to the project folder:
   ```bash
   git clone https://github.com/priyansh2120/cursed-apple.git
   cd cursed-apple
   ```

2. Install the necessary dependencies for the server and client:
   ```bash
   npm install
   ```

3. Set up your `.env` files using the provided templates for each module.

4. Start each service (LLM, Server, and Client) as described.

---

## Environment Variables

Ensure you set up the environment variables in the `.env` files for each module (LLM, server, client) based on the provided template.

---

## License

This project is licensed under the MIT License.

---

### Deploy on AWS EC2
You can deploy the entire project on an AWS EC2 instance. After installation and setup, start the services as mentioned in the **Usage** section.

