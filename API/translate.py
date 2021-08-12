import http.client
import json

conn = http.client.HTTPSConnection("google-translate1.p.rapidapi.com")

sourceLanguage="en"
targetLanguage="ar"
phrase=input("phrase=")
payload=f"q={phrase}&target={targetLanguage}&source={sourceLanguage}"

headers = {
    'content-type': "application/x-www-form-urlencoded",
    'accept-encoding': "application/gzip",
    'x-rapidapi-key': "eb75f98d9dmsh962f61249110833p159325jsnaf5615fe0c9a",
    'x-rapidapi-host': "google-translate1.p.rapidapi.com"
    }

conn.request("POST", "/language/translate/v2", payload, headers)

res = conn.getresponse()
data = res.read()


print(data.decode("utf-8"))
response = json.loads(data.decode("utf-8"))
translatedText = response['data']['translations'][0]['translatedText']
if(targetLanguage in ['ar','ur']):
    print(translatedText[::-1])
else:    
    print(translatedText)
