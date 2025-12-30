# mcp-client-server

Monorepo containing MCP client and server implementations.


## 🧪 Testing the MCP Server Using Cursor (MCP Host)
The terminal_server has been independently tested using Cursor IDE acting as an MCP host/client, validating that the server works correctly outside of the custom MCP client.

This setup confirms that the server:

- Is MCP-compatible
- Can be discovered and launched by an MCP host
- Correctly exposes tools and responds to requests

## 🧩 Cursor MCP Configuration
Cursor MCP Configuration File

Create or update the following file: {PATH}\Admin\.cursor\mcp.json
```json
{
  "mcpServers": {
    "terminal": {
      "command": "{YOUR_python.exe_PATH}\\terminal_server\\.venv\\Scripts\\python.exe",
      "args": [
        "{YOUR_main.py_PATH}\\terminal_server\\main.py"
      ],
      "cwd": "{PROJECT_PATH}\\terminal_server"
    }
  }
}

```
**Configuration Breakdown**

- command
  - Points to the Python interpreter inside the server’s virtual environment

- args
  - Launches the MCP server entry point (main.py)

- cwd
  - Sets the working directory for correct environment and file resolution

This ensures Cursor launches the MCP server exactly as intended.

## ▶️ Running and Testing via Cursor
Open Cursor IDE
- Ensure the mcp.json file is detected
- Start an MCP-enabled chat on cursor IDE
- Cursor launches the terminal_server, fallow instruction on `terminal_server` to configure/start mcp server.
- MCP tools exposed by the server become available for use
- Provide the promt on cursor chat.

## 🔗 Related Modules

- **MCP Client (Gemini-based)**: [`mcp-cleint/`](./mcp-cleint)
- **Terminal MCP Server**: [`terminal_server/`](./terminal_server)

