"""Simple test script to verify the MCP server is working"""
import json
import subprocess
import sys

# Test message: initialize request (required first message in MCP protocol)
init_message = {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "initialize",
    "params": {
        "protocolVersion": "2024-11-05",
        "capabilities": {},
        "clientInfo": {
            "name": "test-client",
            "version": "1.0.0"
        }
    }
}

# Send the message to the server
process = subprocess.Popen(
    [sys.executable, "main.py"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

# Send init message
stdout, stderr = process.communicate(json.dumps(init_message) + "\n")

print("Server response:")
print(stdout)
if stderr:
    print("Server errors:")
    print(stderr)

