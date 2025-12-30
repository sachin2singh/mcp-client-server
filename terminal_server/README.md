# Terminal MCP Server (Python, uv)

This project implements a **terminal-based MCP server** using Python and **`uv`** for dependency and environment management.

The server is designed to work with an MCP client (located in the sibling `mcp-cleint` module) and provides a lightweight, stdio-based execution environment suitable for learning and experimenting with the **Model Context Protocol (MCP)**.

## 📁 Project Structure
<img width="302" height="269" alt="image" src="https://github.com/user-attachments/assets/32976e6e-e990-486f-b5d4-5e72de10816a" />


## 🧠 Purpose

The Terminal MCP Server is responsible for:

- Starting an MCP-compatible server process
- Exposing tools and commands to MCP clients
- Handling client requests over stdio
- Returning structured responses according to MCP expectations

This implementation focuses on **clarity and correctness**, making it ideal for:
- MCP protocol exploration
- Client–server interaction testing
- Tool execution experiments


## 🛠️ Prerequisites

- Python 3.12+
- [`uv`](https://github.com/astral-sh/uv) installed

Verify installation:

```bash
uv --version
```
## 🚀 Setup Instructions (using uv)
1️⃣ Create Virtual Environment and activate
```bash
uv venv
source .venv/Scripts/activate   # Windows (Git Bash)
```
2️⃣ Install Dependencies
Dependencies are defined in pyproject.toml.
```bash
uv sync
```
▶️ Running the Server
From the terminal_server directory:
```bash
uv run python main.py
```

## 🧩 Code Overview
main.py
- Entry point for the MCP server
- Initializes server runtime
- Registers tools and handlers
- Manages request/response lifecycle
test_mcp_tool.py
- Tests individual MCP tool implementations
- Validates tool input/output behavior
test_server.py
- Tests server startup and basic request handling
- Useful for regression and protocol validation

## 🧪 Testing
Run tests from the /terminal_server:
```bash
uv run test_mcp_tool.py
```

## 🤝 Related Projects

- MCP Client: mcp-cleint/
- Parent Repository: mcp-client-server

## 📌 Notes

- This server uses stdio as the primary transport
- Environment variables can be configured via .env
- The project is intentionally minimal and extensible

