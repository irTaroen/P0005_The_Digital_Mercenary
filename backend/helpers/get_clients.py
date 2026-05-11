import json
import os
def get_client(name: str) -> dict | None:
    with open("../clients.json", "r") as f:
        clients = json.load(f)
    client = next((c for c in clients if c["name"] == name), None)
    if not client:
        raise ValueError(f"Client '{name}' not found")
    return client