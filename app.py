import os
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("LinkedIn MCP")

@mcp.tool()
def get_server_status() -> str:
    return "Le serveur MCP LinkedIn est opérationnel et connecté à Perisclaw."

if __name__ == "__main__":
    mcp.run(transport="sse")
