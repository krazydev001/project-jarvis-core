# core/search.py
import os
import requests
from dotenv import load_dotenv

# Explicitly load from your custom config file name
load_dotenv("api.env")

def google_search(query: str) -> str:
    """Performs a live Google Search via Serper.dev and returns a summary snippet."""
    url = "https://google.serper.dev/search"
    api_key = os.getenv("SERPER_API_KEY")
    
    if not api_key:
        return "Search error: Serper API key is missing inside api.env."

    headers = {
        'X-API-KEY': api_key,
        'Content-Type': 'application/json'
    }
    payload = {"q": query, "num": 3}

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=5)
        if response.status_code == 200:
            data = response.json()
            snippets = []
            if "organic" in data:
                for item in data["organic"][:3]:
                    snippets.append(f"- {item.get('title')}: {item.get('snippet')}")
            if snippets:
                return "\n".join(snippets)
            return "No relevant web results found."
        return f"Search failed with status code {response.status_code}."
    except Exception as e:
        return f"Error executing search: {str(e)}"