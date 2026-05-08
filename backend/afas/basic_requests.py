import requests

def test_afas_connection(link, token, connector, show_print=False):
    endpoint = f"{link}{connector}"
    headers = {
        'authorization': token,
        'content-type': "application/json; charset=utf-8;"
    }

    response = requests.get(url=endpoint, headers=headers)
    if show_print:
        print(response.json())
    
    if response.status_code == 200:
        print("Connection successful")
        return True
    else:
        print("Connection failed")
        return False


def get_afas_data(link, token, connector, params, show_print=False):
    params_take_all = "skip=-1&take=-1"
    endpoint = f"{link}{connector}?{params}&{params_take_all}"
    headers = {
        'authorization': token,
        'content-type': "application/json; charset=utf-8;"
    }

    response = requests.get(url=endpoint, headers=headers)

    statuscode = response.status_code

    if show_print:
        omgeving = "TEST" if "resttest" in link else "LIVE"
        print(f"{omgeving} - {connector}: {statuscode}")

    if statuscode == 200:
        return response.json()['rows']
    else:
        return []
