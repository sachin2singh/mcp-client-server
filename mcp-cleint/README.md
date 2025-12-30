# MCP Client (Python, uv)

This project contains a **Python-based MCP client** implemented using **`uv`** and **`Google Gemini Model`**for dependency and environment management.

The client is designed to communicate with an MCP-compatible server (for example, the terminal-based server in the parent repository) and serves as a hands-on learning implementation of the **Model Context Protocol (MCP)**.

## 📁 Project Structure

mcp-cleint/
├── README.md
├── client.py
├── requirements.txt
└── pyproject.toml

## 🧠 Purpose

The MCP client is responsible for:

- Initializing an MCP client runtime
- Sending requests to an MCP server
- Receiving and processing server responses
- Acting as a foundation for MCP protocol experimentation

This project prioritizes **simplicity, clarity, and extensibility**, making it suitable for learning and prototyping.

## 🛠️ Prerequisites

- Python 3.12+
- [`uv`](https://github.com/astral-sh/uv) installed
- Google Gemini API Key (Free Tier)
Verify `uv` installation:
```bash 
uv --version
```

## 🔑 Google Gemini API Key (Free Tier)

**What you need**

- A Google account
- No credit card required for the free tier (usage limits apply)

**How to create a free Gemini API key**
- Go to Google AI Studio
   👉 https://aistudio.google.com
- Sign in with your Google account
- Click “Get API key” (top-right corner)
- Create a new API key
- Copy the generated key


## 🚀 Setup Instructions (using uv)
1️⃣ Initialize the Project
This creates the pyproject.toml and initializes the project.
```bash
uv init mcp-cleint
```

2️⃣ Create and Activate Virtual Environment
```bash
uv venv
source .venv/Scripts/activate   # Windows (Git Bash)
```

3️⃣ Install Dependencies
```bash
uv add -r requirements.txt
```

▶️ Running the MCP Client with Terminal Server
From the mcp-cleint directory, run:
```bash
uv run client.py ../../terminal_server/main.py
```
What this does
- Starts the MCP client
- Launches the terminal-based MCP server
- Sends user prompts to Gemini
- Allows Gemini to invoke MCP tools when appropriate

## 🧩 Code Overview
client.py

- Client initialization logic
- Server startup invocation
- Request/response handling scaffolding

This file will evolve to include:

- MCP JSON-RPC messaging
- Protocol negotiation
- Tool invocation handling

## 🔮 Future Enhancements

- Planned improvements include:
- Full MCP JSON-RPC compliance
- stdio-based and socket-based transports
- Structured logging
- Error handling and retries
- Automated tests

## 🤝 Related Projects

Terminal MCP Server: Located in terminal_server/ at the repository root

Parent Repository: mcp-client-server

## 📌 Notes

This project uses uv for fast dependency resolution and virtual environment management

Each module in the monorepo is intentionally self-contained

Folder name mcp-cleint is kept as-is for now


