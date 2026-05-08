import os
import json5
from dotenv import load_dotenv
from pprint import pprint

from afas.connection_config import create_afas_connection_config
from afas.basic_requests import test_afas_connection
from flows.verloefboekingen import get_verloefboekingen

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
    all_clients = list(client_tokens.keys())

    CLIENT = "Voxtur"
    OMGEVING = "TEST"
    CONFIG = get_client(CLIENT)

    # Create AFAS connection data
    afas_connection_data = create_afas_connection_config(CONFIG["omgeving"], CONFIG["token_live"], CONFIG["token_test"])[OMGEVING]
    afas_base = afas_connection_data["base"]
    afas_token = afas_connection_data["token_encoded"]


    # Connectoren
    connectoren = json5.load(open("config/get_connectors.json"))
    connector_connection = connectoren["connection"]

    # Test connection
    afas_connection_test_data = test_afas_connection(afas_base, afas_token, connector_connection)

    if afas_connection_test_data:
        get_verloefboekingen(afas_connection_data, connectoren)

  