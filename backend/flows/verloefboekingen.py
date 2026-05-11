import json
import os
from afas.basic_requests import get_afas_data


path_connectoren = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "config", "get_connectors.json"))
connectoren = json.load(open(path_connectoren))

def get_verloefboekingen(afas_connection_data):
    afas_link = afas_connection_data["link"]
    afas_token = afas_connection_data["token_encoded"]

    # Connectoren
    connector_verlofboekingen = connectoren["verlofboekingen"]

    afas_verlofboekingen = get_afas_data(afas_link, afas_token, connector_verlofboekingen, "")
    return afas_verlofboekingen