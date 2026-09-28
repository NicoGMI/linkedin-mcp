import os
import requests
from mcp.server.fastmcp import FastMCP

port = int(os.environ.get("PORT", 8000))
mcp = FastMCP("linkedin-n1c0", host="0.0.0.0", port=port)

LINKEDIN_TOKEN = os.getenv("LINKEDIN_ACCESS_TOKEN", "")
ORG_ID = os.getenv("LINKEDIN_ORG_ID", "")

HEADERS = {
    "Authorization": f"Bearer {LINKEDIN_TOKEN}",
    "X-Restli-Protocol-Version": "2.0.0",
    "LinkedIn-Version": "202401",
    "Content-Type": "application/json"
}

@mcp.tool()
def get_recent_mentions_and_comments() -> str:
    """Récupère les derniers commentaires et mentions sous les posts N1c0."""
    url = f"https://api.linkedin.com/rest/socialActions/urn:li:organization:{ORG_ID}/comments"
    resp = requests.get(url, headers=HEADERS)
    return resp.text if resp.status_code == 200 else f"Erreur {resp.status_code}: {resp.text}"

@mcp.tool()
def reply_to_comment(parent_comment_urn: str, message: str) -> str:
    """Poste une réponse à un commentaire ou tag sur LinkedIn au nom de N1c0."""
    url = f"https://api.linkedin.com/rest/socialActions/{parent_comment_urn}/comments"
    payload = {
        "actor": f"urn:li:organization:{ORG_ID}",
        "message": {"text": message}
    }
    resp = requests.post(url, headers=HEADERS, json=payload)
    return "Réponse publiée !" if resp.status_code in [200, 201] else f"Erreur {resp.status_code}: {resp.text}"

if __name__ == "__main__":
    mcp.run(transport="sse")
