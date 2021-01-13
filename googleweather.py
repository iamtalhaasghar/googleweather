# Python Script to scrap weather info from Google
 
import requests
from bs4 import BeautifulSoup
import sys


user_agent = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
city_name = '+'.join(sys.argv[1:])
google_url='https://www.google.com/search?q=weather+%s&h1=en' % city_name
response=requests.get(google_url, headers=user_agent)
response.raise_for_status()

soup=BeautifulSoup(response.text, 'html.parser')
city=soup.find(id = "wob_loc")
time=soup.find(id = 'wob_dts')
condition=soup.find(id = 'wob_dc')
tempC = soup.find(id = 'wob_tm')
tempF = soup.find(id = 'wob_ttm')
precipitation = soup.find(id = 'wob_pp')
humidity = soup.find(id = 'wob_hm')
wind_kmh = soup.find(id = 'wob_ws')
wind_mph = soup.find(id = 'wob_tws')

print("\n%s\n%s\n%s\n%s\u00b0C \u2248 %s\u00b0F\nPrecipitation: %s\nHumidity: %s\nWind: %s \u2248 %s" % 
	(city.text.strip(), time.text.strip(),condition.text.strip(), tempC.text.strip(), tempF.text.strip(),precipitation.text.strip(), humidity.text.strip(),
	wind_kmh.text.strip(), wind_mph.text.strip()))