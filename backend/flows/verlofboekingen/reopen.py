import json
import os
from afas.basic_requests import get_afas_data, put_afas_data
import time
from pprint import pprint

def reopen_verlofboekingen(afas_connection_data, get_connectoren, update_connectoren, reden):
    afas_link = afas_connection_data["link"]
    afas_token = afas_connection_data["token_encoded"]

    # Connectoren
    connector_verlofboekingen = get_connectoren["verlofboekingen"]
    connector_verlofboekingen_update = update_connectoren["verlofboekingenID"]

    afas_verlofboekingen = get_afas_data(afas_link, afas_token, connector_verlofboekingen, "")
    print(len(afas_verlofboekingen))

    for item in afas_verlofboekingen:
        regel_id = item["regelnummer"]
        # print(regel_id)
        payload = {
            "HrAbsenceID": {
                "Element": {
                "@Id": item["regelnummer"],
                "@EmId": item["medewerker"],
                "Fields": {
                    "ViAt": item["typeVerlof"],
                    "DaBe": item["beginDatum"].rstrip("Z"),
                    "DaEe": item["eindDatum"].rstrip("Z"),
                    "Re": reden,
                    "LeDt": item["gedeeltelijk"]
                }
                }
            }
            }

        statuscode = put_afas_data(afas_link, afas_token, connector_verlofboekingen_update, payload)
        if statuscode == 201:
            print(f"Data updated successfully for regelnummer: {regel_id}")
        else:
            print(f"Failed to update data for regelnummer: {regel_id} with status code: {statuscode}")