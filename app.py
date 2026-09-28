import os
import uvicorn
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("LinkedIn MCP")

@mcp.tool()
def get_server_status() -> str:
    return "Le serveur LinkedIn MCP est opérationnel et connecté à Perisclaw."

app = mcp.sse_app()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)
