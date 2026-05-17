import json
import os
from afas.basic_requests import get_afas_data, put_afas_data

def reopen_verlofboekingen(afas_connection_data, get_connectoren, update_connectoren, reden):
    afas_link = afas_connection_data["link"]
    afas_token = afas_connection_data["token_encoded"]

    # Connectoren
    connector_verlofboekingen = get_connectoren["verlofboekingen"]
    connector_verlofboekingen_update = update_connectoren["verlofboekingen"]

    afas_verlofboekingen = get_afas_data(afas_link, afas_token, connector_verlofboekingen, "")

    for item in afas_verlofboekingen:
        payload = {
            "HrAbsenceID": {
                "Element": {
                "@Id": item["regelnummer"],
                "@EmId": item["medewerker"],
                "Fields": {
                    "ViAt": item["typeVerlof"],
                    "DaBe": item["beginDatum"].rstrip("Z"),
                    "Re": reden,
                    "LeDt": item["gedeeltelijk"]
                }
                }
            }
            }

        put_afas_data(afas_link, afas_token, connector_verlofboekingen_update, payload)
     