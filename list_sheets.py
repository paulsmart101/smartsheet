import requests, json
url = 'https://api.smartsheet.com/2.0/sheets'
payload = {}
headers = {  'Authorization': 'Bearer xxxxxxxxxxxxxxxxxxxxxxxxx'}
response = requests.request('GET', url, headers = headers, data = payload, allow_redirects=False)
parsed = json.loads(response.text)
#print(json.dumps(parsed, indent=4, sort_keys=True))
print(len(parsed['data']),"sheets\n\n")
for sheet in parsed['data']:
    print('ID: {:<20} Name: {:40}'.format(sheet['id'],sheet['name']))
