import http.client

conn = http.client.HTTPSConnection("api.quran.com")

payload = "{}"

conn.request("GET", "/api/v4/verses/random?words=true&language=en", payload)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))