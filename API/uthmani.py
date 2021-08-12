import http.client

conn = http.client.HTTPSConnection("api.quran.com")

payload = "{}"

juz_number = 10
page_number = 1

url = f"/api/v4/quran/verses/uthmani_simple?juz_number={juz_number}&page_number={page_number}"
conn.request("GET", url, payload)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
