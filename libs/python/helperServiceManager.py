import requests
import os

SM_SERVICE_BINDING_URL = os.environ.get("BTPSA_SM_BINDING_URL")
SM_SERVICE_BINDING_CLIENT_ID = os.environ.get("BTPSA_SM_CLIENT_ID")
SM_SERVICE_BINDING_CLIENT_SECRET = os.environ.get("BTPSA_SM_CLIENT_SECRET")
SM_SERVICE_BINDING_SM_URL = os.environ.get("BTPSA_SM_SM_URL")


def getToken():

    url = SM_SERVICE_BINDING_URL + "/oauth/token?grant_type=client_credentials"

    try:
        p = requests.post(url, auth=(SM_SERVICE_BINDING_CLIENT_ID, SM_SERVICE_BINDING_CLIENT_SECRET))
        result = p.json()
        print(result)

    except:
        result = None
