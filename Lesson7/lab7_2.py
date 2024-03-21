import requests
import pprint

headers = {
        "accept": "application/yang-data+json",
        "Content-Type": "application/yang-data+json"
        }

URL = "https://10.31.70.209/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces"

r = requests.get(
    URL,
    verify=False,
    auth=("restapi", "j0sg1280-7@"),
    headers=headers,
)

if r.status_code == 200:
    data = r.json()
    # pprint.pprint(data, width=30)
    for current_int in data['Cisco-IOS-XE-interfaces-oper:interfaces']['interface']:
        print("Interface: ", current_int['name'])
        print("Input packets/bytes: ", current_int['statistics']['in-unicast-pkts'], "/", current_int['statistics']['in-octets'])
        print("Output packets/bytes: ", current_int['statistics']['out-unicast-pkts'], "/", current_int['statistics']['out-octets'])