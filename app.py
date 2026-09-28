import os
from mcp.server.fastmcp import FastMCP

Initialisation du serveur FastMCP
mcp = FastMCP("LinkedIn MCP")

@mcp.tool()
def get_server_status() -> str:
    """Retourne le statut du serveur LinkedIn MCP."""
    return "Le serveur MCP LinkedIn est opérationnel et connecté à Perisclaw."

if __name__ == "__main__":
    # Lancement du serveur SSE FastMCP
    mcp.run(transport="sse")
