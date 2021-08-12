import http.client

conn = http.client.HTTPSConnection("loqate-address.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "eb75f98d9dmsh962f61249110833p159325jsnaf5615fe0c9a",
    'x-rapidapi-host': "loqate-address.p.rapidapi.com"
    }

conn.request("GET", "/rest/?p=v%2Bg&lqtkey=14dea8c6fggh51yt7b1c8d477994542b7f115009&opts=DefaultCountry%3DUSA%2COutputScript%3DLatn&maxresults=10&outputfields=Address1%2CAddress2%2CAddress3%2CAddress4%2CCountryName&fs=no&ctry=United%20States&add6=USA&add5=94066&add4=CA&add3=San%20Bruno&add2=Suite%20290&add1=1111%20bayhill%20dr&addr=1111%20bayhill%20dr%20san%20bruno%20USA", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))