#Importing necessary packages
from plyer import notification
import requests
import json
#C = K - 273.15.
city=input('Enter your city name or pincode ')
city.replace(' ',',')
#get your key from api.openweathermap.org
api_key='your api key '
url=(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}')
title=f'{city} weather notifcation'
def notify(url,title):
    try:
        response=requests.get(url)
    except Exception as e:
        notification.notify(message='Please check your internet connection') 
    #load the json response in form of text
    weather=json.loads(response.text)
    
    #itering values from json response
    for weather_desc in weather['weather']:        
        weather_description=weather_desc['description']
    actual_temp=int(float(weather['main']['temp'])-273.15)
    max_temp=int(float(weather['main']['temp_max'])-273.15)
    city_name=weather["name"]

    #concating all the values in single string
    weather_details=f'{weather_description} in {city_name} with a temperature of {actual_temp}° C and maximum temperature can be {max_temp}° C .' 
    print(weather_details)   
    notification.notify(title=title,message=weather_details,app_icon=None,timeout=10,toast=False)
        

#calling the function
notify(url,title)