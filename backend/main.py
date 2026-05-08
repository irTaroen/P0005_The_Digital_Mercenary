import os
import json5
from dotenv import load_dotenv
from pprint import pprint

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))

raw = os.getenv("CLIENT_TOKENS", "{}")
client_tokens: dict = json5.loads(raw)


def get_client(name: str) -> dict:
    """Return the token config for a client by name."""
    client = client_tokens.get(name)
    if client is None:
        raise KeyError(f"No config found for client '{name}'")
    return client


if __name__ == "__main__":
    print("All clients:", list(client_tokens.keys()))

    client_name = "Essers"
    config = get_client(client_name)
    print(f"{client_name} config:")
    pprint(config)
