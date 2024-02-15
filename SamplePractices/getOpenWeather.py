#!/usr/bin/python3
import json, sys, requests
APPID = '6f05cf90facd91e658e64336aacff516'
if len(sys.argv) < 2:
    print('Usage: getOpenWeather.py city_name 2-letter_country_code')
    sys.exit()
location = ''.join(sys.argv[1:])

url ='https://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3&APPID=%s ' % (location, APPID)
response  = requests.get(url)
response.raise_for_status()
print(response.text)