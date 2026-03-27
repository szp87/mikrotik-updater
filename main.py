import requests
import json
from bs4 import BeautifulSoup

def pobierz_wersje(architektura):
    url = f"https://mikrotik.com/download?architecture={architektura}"
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # szukamy tagu który ma wire:snapshot z "channel":"stable"
    for tag in soup.find_all(attrs={"wire:snapshot": True}):
        snapshot_raw = tag.get("wire:snapshot")
        snapshot = json.loads(snapshot_raw)
        data = snapshot.get("data", {})
        if data.get("channel") == "stable":
            return data.get("version")

    return None

print(pobierz_wersje("arm"))
print(pobierz_wersje("arm64"))


