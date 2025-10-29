import datetime as dt
import requests
from dotenv import load_dotenv
import os
load_dotenv()
def K_to_c(tempkelvin):
        celcius=tempkelvin-273.15
        return celcius
def temperature(city):
    API_KEY=os.getenv("weather_api_key")
    BASE_URL="http://api.openweathermap.org/data/2.5/weather"
    city=city
    params={
        "q":city,
        "appid":API_KEY
    }
    response=requests.get(BASE_URL,params=params)
    data=response.json()


    tempcelcuis=round(K_to_c(data['main']['temp']),2)
    mintemp=round(K_to_c(data['main']['temp_min']),2)
    description=data['weather'][0]['description']

    return f"""Today's weather is {description},with a  temperature of {tempcelcuis} degrees Celsius and minimum temperature of {mintemp} degree Celsius."""


