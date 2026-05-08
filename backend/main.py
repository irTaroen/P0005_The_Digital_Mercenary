import os
import json5
from dotenv import load_dotenv
from pprint import pprint

from afas.connection_config import create_afas_connection_config
from afas.basic_requests import get_afas_data, test_afas_connection

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
    CLIENT = "Voxtur"
    OMGEVING = "TEST"
    # print("All clients:", list(client_tokens.keys()))

    config = get_client(CLIENT)
    # print(f"{CLIENT} config:")

    # Create AFAS connection data
    afas_connection_data = create_afas_connection_config(config["omgeving"], config["token_live"], config["token_test"])[OMGEVING]
    afas_base = afas_connection_data["base"]
    afas_link = afas_connection_data["link"]
    afas_token = afas_connection_data["token_encoded"]


    # Connectoren
    connectoren = json5.load(open("config/get_connectors.json"))
    connector_connection = connectoren["connection"]
    connector_verlofboekingen = connectoren["verlofboekingen"]

    # Test connection
    afas_connection_test_data = test_afas_connection(afas_base, afas_token, connector_connection)

    # Get verlofboekingen
    afas_verlofboekingen = get_afas_data(afas_link, afas_token, connector_verlofboekingen, "")
    pprint(len(afas_verlofboekingen))