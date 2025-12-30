"""Test script to directly call the MCP server's run_command tool"""
import asyncio
import sys
import os

# Add the current directory to path to import main
sys.path.insert(0, os.path.dirname(__file__))

from main import run_command

async def test_create_directory():
    """Test creating a directory through the MCP server tool"""
    print("Testing MCP server's run_command tool...")
    print(f"Workspace: D:\\course\\mcp\\workspace")
    print("\n1. Creating test directory via MCP server...")
    
    # Create a directory using the MCP tool
    result = await run_command("mkdir test_mcp_directory")
    print(f"Result: {result}")
    
    print("\n2. Creating a file via MCP server...")
    result = await run_command("echo 'Created via MCP server' > test_mcp_directory\\test_file.txt")
    print(f"Result: {result}")
    
    print("\n3. Listing contents via MCP server...")
    result = await run_command("dir test_mcp_directory")
    print(f"Result:\n{result}")
    
    print("\nMCP server tool test completed!")

if __name__ == "__main__":
    asyncio.run(test_create_directory())

