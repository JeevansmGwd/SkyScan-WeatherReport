import requests
import json

def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"
    
    response = requests.get(complete_url)
    
    weather_data = response.json()
    
  
    if weather_data['cod'] != '404':
        main = weather_data['main']
        wind = weather_data['wind']
        weather = weather_data['weather'][0]

        temperature = main['temp']
        pressure = main['pressure']
        humidity = main['humidity']
        wind_speed = wind['speed']
        description = weather['description']
        
      
        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Pressure: {pressure} hPa")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
        print(f"Description: {description}")
    else:
        print("City Not Found!")

if __name__ == "__main__":
  
    city = input("Enter city name: ")
    api_key = "Replace with API Key"  
    
    get_weather(city, api_key)
