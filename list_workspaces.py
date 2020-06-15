import requests, json
url = 'https://api.smartsheet.com/2.0/workspaces'
payload = {}
headers = {  'Authorization': 'Bearer xxxxxxxxxxxxxxxxxx'}
response = requests.request('GET', url, headers = headers, data = payload, allow_redirects=False)
parsed = json.loads(response.text)
#print(json.dumps(parsed, indent=4, sort_keys=True))
for workspace in parsed['data']:
    print(workspace['name'])
