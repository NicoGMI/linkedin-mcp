import os
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI(title="LinkedIn MCP Server")

@app.get("/")
@app.get("/sse")
def health_check():
    return {"status": "running", "service": "LinkedIn MCP"}

@app.post("/")
@app.post("/sse")
async def mcp_endpoint(request: Request):
    try:
        body = await request.json()
    except Exception:
        return JSONResponse({"error": "Invalid JSON"}, status_code=400)
    
    req_id = body.get("id")
    method = body.get("method")
    params = body.get("params", {})
    
    if method == "initialize":
        return JSONResponse({
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "LinkedIn MCP", "version": "1.0.0"}
            }
        })
    elif method == "notifications/initialized":
        return JSONResponse({"jsonrpc": "2.0", "result": {}})
    elif method == "tools/list":
        return JSONResponse({
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "get_server_status",
                        "description": "Statut du serveur LinkedIn MCP",
                        "inputSchema": {"type": "object", "properties": {}}
                    }
                ]
            }
        })
    elif method == "tools/call":
        return JSONResponse({
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "content": [{"type": "text", "text": "Le serveur MCP LinkedIn est opérationnel et connecté à Perisclaw."}]
            }
        })
    elif method == "ping":
        return JSONResponse({"jsonrpc": "2.0", "id": req_id, "result": {}})
    else:
        return JSONResponse({"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": f"Method not found: {method}"}})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)
