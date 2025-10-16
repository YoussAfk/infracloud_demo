### Shorter version of the two previous cells

### STEP 1 PREF
import requests
import datetime
import json

# Suppress credential warning for this exercise
requests.packages.urllib3.disable_warnings()
print("Current date and time: ")
print(datetime.datetime.now())

# HARD CODED VARIABLES
DNAC_scheme = 'https://'
DNAC_authority = 'sandboxdnac2.cisco.com'
# DNAC_port=':443'
DNAC_path_token = '/dna/system/api/v1/auth/token'
DNAC_path = '/dna/intent/api/v1/network-device'
DNAC_user = input("Username? (devnetuser) ")
DNAC_psw = input("Password? (Cisco123!) ")

### STEP 2 TOKEN REQUEST
token_req_url = DNAC_scheme + DNAC_authority + DNAC_path_token
auth = (DNAC_user, DNAC_psw)
req = requests.post(token_req_url, auth=auth, verify=False)
print("API Return Code = " + str(req.status_code))
print("Request URI: " + token_req_url)
print("Username: " + DNAC_user)
resp = req.text
print(req.text)
token = req.json()['Token']
print("Received Token:")
print(token)
### STEP 3
#REQUEST API SERVICE (USING X-AUTH-TOKEN) -- INVENTORY REQUEST
import datetime
print("Current date and time: ")
print(datetime.datetime.now())
print('Inventory Request - Network Devices')

# INVENTORY REQUEST
req_url = DNAC_scheme+DNAC_authority+DNAC_path
print(req_url)
header_data = {'x-auth-token': token}
resp_devices = requests.request('GET', req_url, headers=header_data, verify=False)
print(resp_devices)
resp_devices_json = resp_devices.json()
#print(resp_devices)
#print(json.loads(resp_devices.text))
dev_dict = json.loads(resp_devices.text)
print(dev_dict['response'][0].keys())
print('-------------------------------')
#print(type(resp_devices_json))
print("Response (json):")
print(json.dumps(resp_devices_json, indent=2))
#### keys
#### print(resp_devices_json.keys())
i = 1
ip_address = resp_devices_json["response"][i]["managementIpAddress"]
update_time = resp_devices_json["response"][i]["lastUpdated"]
err_msg = resp_devices_json["response"][i]["errorDescription"]

print(ip_address)
print(update_time)
print(err_msg)
for device in resp_devices_json['response']:
    ip_address = device["managementIpAddress"]
    print(ip_address)
    update_time = device["lastUpdated"]
    print(update_time)
    err_msg = device["errorDescription"]
    print(err_msg)
    collection_status = device["collectionStatus"]
    print(collection_status)



