import base64


def encode_base64_token(text):
    return base64.b64encode(text.encode("utf-8")).decode("utf-8")


def create_afas_connection_data(omgeving_id, token_live, token_test):
    base_live = f"https://{omgeving_id}.rest.afas.online/ProfitRestServices"
    base_test = f"https://{omgeving_id}.resttest.afas.online/ProfitRestServices"
    return {
        "LIVE": {
            "base": f"{base_live}/",
            "link": f"{base_live}/connectors/",
            "fileconnector": f"{base_live}/fileconnector/",
            "token_decoded": token_live,
            "token_encoded": f"AfasToken {encode_base64_token(token_live)}",
        },
        "TEST": {
            "base": f"{base_test}/",
            "link": f"{base_test}/connectors/",
            "fileconnector": f"{base_test}/fileconnector/",
            "token_decoded": token_test,
            "token_encoded": f"AfasToken {encode_base64_token(token_test)}",
        },
    }
