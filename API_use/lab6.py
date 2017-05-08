import urllib.parse,urllib.request
import json
import ssl


def findlocation():
    base_url = 'https://maps.googleapis.com/maps/api/place/details/json'

    values = dict()
    values['placeid'] = 'ChIJy_fxa0CuPIgRWmk6N0CQ0u8'
    values['key'] = 'AIzaSyC4UWR7ruzWyiWcDyHLKqb1wVQL8XpquG0' 

    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    data = urllib.parse.urlencode(values)

    full_url = base_url + '?' + data
    req = urllib.request.Request(full_url)

    with urllib.request.urlopen(req, context=ctx) as response:
        response_str = response.read().decode()

    json_response = json.loads(response_str)

    if json_response["status"]:
        loc=json_response["result"]["geometry"]["location"]
        lat=str(loc["lat"])
        lng=str(loc["lng"])
        print("latitude="+lat,"and","longitude="+lng)
    else:
        "No result!"



def restaurants():
    way = input("Enter a way to sort (rating or price):")
    base_url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'

    values = dict()
    values['location'] = "42.280738," + "-83.7401718"
    values["radius"] = 500
    values['key'] = 'AIzaSyC4UWR7ruzWyiWcDyHLKqb1wVQL8XpquG0' 
    values["type"] = "restaurant"

    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    data = urllib.parse.urlencode(values)

    full_url = base_url + '?' + data

    req = urllib.request.Request(full_url)

    with urllib.request.urlopen(req, context=ctx) as response:
        response_str = response.read().decode()

    json_response = json.loads(response_str)
    rat=dict()
    pri=dict()

    if json_response["status"]:
        res = json_response["results"]
        for item in res:
            rat[item["name"]]=float(item["rating"])
            pri[item["name"]]=float(item.get("price_level",0.0))
    print(rat)
    if way=="rating":
        rat = sorted(rat.items(), key=lambda x: x[1], reverse=False)
        for item in rat:
            print(item[0])
    elif way=="price":
        pri = sorted(pri.items(), key=lambda x: x[1], reverse=False)
        for item in pri:
            print(item[0])
    else:
        print("Invalid")

