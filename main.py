import requests,json
import socket
import threading

import urllib.request
external_ip = urllib.request.urlopen('https://ident.me%27%29.read%28%29.decode%28%27utf8%27%29/
print(external_ip)
pygame.init()
respounse=requests.get(url=f'http://ip-api.com/json/%7Bexternal_ip%7D').json()
print(respounse['city'])
screen =pygame.display.set_mode((1000,1000))
api_key="f5ea1444ac76d17489d97833763c006c"
url = "https://api.openweathermap.org/data/2.5/weather?q="
city=respounse['city']
full = url+city+"&appid="+api_key
res = requests.get(full)
data = res.json()
print(data["weather"][0]['main'])
