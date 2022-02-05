# Python CLI tool to Scrap weather info from Google
 

def query_weather(city_name):
    import requests
    from bs4 import BeautifulSoup

    user_agent = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
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

    print("%s\n%s\n%s\u00b0C \u2248 %s\u00b0F\nPrecipitation: %s\nHumidity: %s\nWind: %s \u2248 %s\nLast Updated: %s" % 
      (city.text.strip(),condition.text.strip(), tempC.text.strip(), tempF.text.strip(),precipitation.text.strip(),
            humidity.text.strip(),
          wind_kmh.text.strip(), wind_mph.text.strip(), time.text.strip()))
def main():
  import sys
  try:
    query_weather('+'.join(sys.argv[1:]))
  except Exception as ex:
    print(ex)
if __name__== "__main__":
    main()
