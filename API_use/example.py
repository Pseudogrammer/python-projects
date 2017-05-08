import urllib.parse
import urllib.request
import json
import ssl
base_url = 'https://maps.googleapis.com/maps/api/place/queryautocomplete/json'

values = dict()
values['input'] = 'North Quad'
values['key'] = 'AIzaSyC4UWR7ruzWyiWcDyHLKqb1wVQL8XpquG0'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

data = urllib.parse.urlencode(values)

full_url = base_url + '?' + data

req = urllib.request.Request(full_url)

with urllib.request.urlopen(req, context=ctx) as response:
    response_str = response.read().decode()
print(response_str)
json_response = json.loads(response_str)
print ('Request status:', json_response['status'])

predictions = json_response.get('predictions', None)
if predictions:
    print ('Predicted places:')
    for place in predictions:
        print (place['description'])

