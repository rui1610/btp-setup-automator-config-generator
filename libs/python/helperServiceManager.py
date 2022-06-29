import requests
import os

SM_SERVICE_BINDING_URL = os.environ.get("BTPSA_SM_BINDING_URL")
SM_SERVICE_BINDING_CLIENT_ID = os.environ.get("BTPSA_SM_CLIENT_ID")
SM_SERVICE_BINDING_CLIENT_SECRET = os.environ.get("BTPSA_SM_CLIENT_SECRET")
SM_SERVICE_BINDING_SM_URL = os.environ.get("BTPSA_SM_SM_URL")


def getServiceData():
    services = None
    servicePlans = None
    access_token = getToken()

    url = SM_SERVICE_BINDING_SM_URL + "/v1/service_offerings?max_items=10000"
    try:
        p = requests.get(url, headers={"Authorization": "bearer " + access_token})
        services = p.json()["items"]
    except:
        services = None

    url = SM_SERVICE_BINDING_SM_URL + "/v1/service_plans?max_items=10000"
    try:
        p = requests.get(url, headers={"Authorization": "bearer " + access_token})
        servicePlans = p.json()["items"]
    except:
        servicePlans = None

    for service in services:
        id = service.get("id")
        service["servicePlans"] = []
        for plan in servicePlans:
            service_id = plan.get("service_offering_id")
            if service_id == id:
                service["servicePlans"].append(plan)

    return services


def getToken():
    result = None
    url = SM_SERVICE_BINDING_URL + "/oauth/token?grant_type=client_credentials"

    try:
        p = requests.post(url, auth=(SM_SERVICE_BINDING_CLIENT_ID, SM_SERVICE_BINDING_CLIENT_SECRET))
        response = p.json()
        result = response["access_token"]
    except:
        result = None

    return result
