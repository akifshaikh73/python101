import http.client
import json


conn = http.client.HTTPSConnection("community-open-weather-map.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "eb75f98d9dmsh962f61249110833p159325jsnaf5615fe0c9a",
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
    }

city=input("city=")
conn.request("GET", f"/weather?q={city}&lang=null&units=Imperial&mode=xml%2C%20html", headers=headers)

res = conn.getresponse()
data = res.read()
datajson = json.loads(data.decode("utf-8"))
print(datajson)
temp = datajson["main"]["temp"]
print(f"The temperature of {city} is {temp}")
weatherlist = datajson["weather"]
print("Conditions are:")
for w in weatherlist:
    print(w["description"])
#print(data.decode("utf-8"))