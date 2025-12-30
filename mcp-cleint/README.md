# MCP Client (Python, uv)

This project contains a **Python-based MCP client** implemented using **`uv`** for dependency and environment management.

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

Verify `uv` installation:
```bash 
uv --version
```

## 🚀 Setup Instructions (using uv)
1️⃣ Initialize the Project
uv init mcp-cleint
This creates the pyproject.toml and initializes the project.

2️⃣ Create and Activate Virtual Environment
uv venv
source .venv/Scripts/activate   # Windows (Git Bash)

3️⃣ Install Dependencies
uv add -r requirements.txt

▶️ Running the MCP Client
From the mcp-cleint directory, run:
uv run client.py ../../terminal_server/main.py

What this does

Starts the MCP client

Launches the terminal-based MCP server

Establishes client–server communication via the configured transport

🧩 Code Overview
client.py

Main entry point for the MCP client. This file contains:

Client initialization logic

Server startup invocation

Request/response handling scaffolding

This file will evolve to include:

MCP JSON-RPC messaging

Protocol negotiation

Tool invocation handling

🔮 Future Enhancements

Planned improvements include:

Full MCP JSON-RPC compliance

stdio-based and socket-based transports

Structured logging

Error handling and retries

Automated tests

🤝 Related Projects

Terminal MCP Server: Located in terminal_server/ at the repository root

Parent Repository: mcp-client-server

📌 Notes

This project uses uv for fast dependency resolution and virtual environment management

Each module in the monorepo is intentionally self-contained

Folder name mcp-cleint is kept as-is for now


