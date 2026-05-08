from afas.basic_requests import get_afas_data
from pprint import pprint

def get_verloefboekingen(afas_connection_data, connectoren):
    afas_link = afas_connection_data["link"]
    afas_token = afas_connection_data["token_encoded"]

    # Connectoren
    connector_verlofboekingen = connectoren["verlofboekingen"]

    afas_verlofboekingen = get_afas_data(afas_link, afas_token, connector_verlofboekingen, "")
    pprint(len(afas_verlofboekingen))