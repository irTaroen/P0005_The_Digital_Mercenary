
from pprint import pprint
import json
import os
from helpers.get_clients import get_client
from afas.connection_config import create_afas_connection_config
from flows.verlofboekingen.reopen import reopen_verlofboekingen

# Get client data
client_name = "Zig"
VERSIE = "LIVE"

# Get connection config
client_data = get_client(client_name)
client_connection_config = create_afas_connection_config(client_data["omgeving"], client_data["token_live"], client_data["token_test"])[VERSIE]

# Get connectors
path_get_connectoren = os.path.abspath(os.path.join(os.path.dirname(__file__), "config", "get_connectors.json"))
path_update_connectoren = os.path.abspath(os.path.join(os.path.dirname(__file__), "config", "update_connectoren.json"))
get_connectoren = json.load(open(path_get_connectoren))
update_connectoren = json.load(open(path_update_connectoren))

verloefboekingen = reopen_verlofboekingen(client_connection_config, get_connectoren, update_connectoren, "Correctie: Toevoegen Project")
