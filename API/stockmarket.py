import http.client
import json

conn = http.client.HTTPSConnection("apidojo-yahoo-finance-v1.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "eb75f98d9dmsh962f61249110833p159325jsnaf5615fe0c9a",
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }

symbol="AAPL"

conn.request("GET", f"/stock/v2/get-summary?symbol={symbol}&region=US", headers=headers)

res = conn.getresponse()
data = res.read()
datajson = json.loads(data.decode("utf-8"))
#print(data.decode("utf-8"))
print(datajson)
with open("stock.json",'w') as stock_file:
    stock_file.write(data.decode("utf-8"))