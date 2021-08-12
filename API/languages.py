import http.client

conn = http.client.HTTPSConnection("google-translate1.p.rapidapi.com")

headers = {
    'accept-encoding': "application/gzip",
    'x-rapidapi-key': "eb75f98d9dmsh962f61249110833p159325jsnaf5615fe0c9a",
    'x-rapidapi-host': "google-translate1.p.rapidapi.com"
    }

conn.request("GET", "/language/translate/v2/languages", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))