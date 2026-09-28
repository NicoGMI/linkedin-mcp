import os
from mcp.server.fastmcp import FastMCP

Initialisation du serveur FastMCP
mcp = FastMCP("LinkedIn MCP")

@mcp.tool()
def get_server_status() -> str:
    """Retourne le statut du serveur LinkedIn MCP."""
    return "Le serveur MCP LinkedIn est opérationnel et connecté à Perisclaw."

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    mcp.run(transport="sse", host="0.0.0.0", port=port)
