
from pprint import pprint

from helpers.get_clients import get_client
from afas.connection_config import create_afas_connection_config
from flows.verloefboekingen import get_verloefboekingen


client_name = "Zig"
VERSIE = "LIVE"
client_data = get_client(client_name)
client_connection_config = create_afas_connection_config(client_data["omgeving"], client_data["token_live"], client_data["token_test"])[VERSIE]

verloefboekingen = get_verloefboekingen(client_connection_config)

