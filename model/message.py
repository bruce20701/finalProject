import weatherQurey
from weather import Weather
from datetime import datetime

weather1 = Weather(weatherQurey.qureyWeatherbyCity("臺北市"))
weather2 = Weather(weatherQurey.qureyNearestTimeWeather(datetime.now().strftime("%H:%M")))
weather1.printWeather()
weather2.printWeather()