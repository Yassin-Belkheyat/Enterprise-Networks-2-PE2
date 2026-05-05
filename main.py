import requests
import json
from requests.auth import HTTPBasicAuth
import urllib3

urllib3.disable_warnings()

ROUTER_IP = "192.168.248.128"
USERNAME = "cisco"
PASSWORD = "cisco123!"

BASE_URL = f"https://{ROUTER_IP}/restconf/data"

HEADERS = {
    "Content-Type": "application/yang-data+json",
    "Accept": "application/yang-data+json"
}

def send_config(endpoint, payload):
    url = BASE_URL + endpoint

    response = requests.patch(
        url,
        headers=HEADERS,
        auth=HTTPBasicAuth(USERNAME, PASSWORD),
        data=json.dumps(payload),
        verify=False
    )

    print(f"URL: {url}")
    print(f"Status code: {response.status_code}")

    if response.status_code in [200, 201, 204]:
        print("Configuratie succesvol toegepast")
    else:
        print("Fout:")
        print(response.text)

def load_json(file_path):
    with open(file_path, "r") as file:
        return json.load(file)

hostname_config = load_json("config/hostname.json")

send_config(
    "/Cisco-IOS-XE-native:native",
    hostname_config
)

def get_config(endpoint):
    url = BASE_URL + endpoint

    response = requests.get(
        url,
        headers=HEADERS,
        auth=HTTPBasicAuth(USERNAME, PASSWORD),
        verify=False
    )

    print(f"GET Status: {response.status_code}")
    print(response.text)

get_config("/Cisco-IOS-XE-native:native/hostname")

interfaces_config = load_json("config/interfaces.json")

send_config(
    "/Cisco-IOS-XE-native:native/interface",
    interfaces_config
)
get_config("/Cisco-IOS-XE-native:native/interface/Loopback=0")
