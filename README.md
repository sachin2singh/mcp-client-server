# ⭐ MCP Terminal Client–Server Framework

A monorepo containing Model Context Protocol (MCP) client and server implementations, designed for terminal-based interactions and extensible client integrations.

## 🔁 Request–Response Flow

- MCP host discovers the terminal server
- Server registers available tools
- Client issues a tool invocation request
- Server executes the command
- Result is returned to the MCP host
  
<img width="3635" height="2445" alt="Untitled diagram-2025-12-31-110555" src="https://github.com/user-attachments/assets/734dead0-6cf2-4c9b-b6d2-c85f66d36782" />


## 🧪 Testing the MCP Terminal Server Using Cursor (MCP Host)
The terminal_server has been independently tested using Cursor IDE acting as an MCP host/client, validating that the server works correctly outside of the custom MCP client.

This setup confirms that the server:

- Is **MCP-compatible**
- Can be **discovered and launched** by an MCP host
- Correctly **exposes tools** and **responds to requests**

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

- **command**
  Points to the Python interpreter inside the server’s virtual environment
- **args**
  Launches the MCP server entry point (main.py)
- **cwd**
  Sets the working directory for correct environment and file resolution

This ensures Cursor launches the MCP server exactly as intended.

## ▶️ Running and Testing via Cursor
Open Cursor IDE
- Ensure the mcp.json file is detected
- Start an MCP-enabled chat on cursor IDE
- Cursor launches the terminal_server, fallow instruction on `terminal_server` to configure/start mcp server.
- MCP tools exposed by the server become available for use
- Provide the promt on cursor chat.
- **Example prompt:**
```text
    Create a directory called "mcp_cursor_client" and then create a file "mcp_client.txt" under it. Write the content "Successfully created direcoty"
```


## 🔗 Related Modules

- **MCP Client (Gemini-based)**: [`mcp-cleint/`](./mcp-cleint)
- **Terminal MCP Server**: [`terminal_server/`](./terminal_server)
- **Terminal MCP Server with Docker support**: [`terminal_server/`](./terminal_server_docker)

