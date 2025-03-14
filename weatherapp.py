import requests

def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"
    response = requests.get(complete_url)
    
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        wind = data['wind']
        weather_desc = data['weather'][0]['description']
        
        temp = main['temp']
        feels_like = main['feels_like']
        humidity = main['humidity']
        wind_speed = wind['speed']
        
        weather_report = (
            f"Weather in {city}:\n"
            f"Temperature: {temp}°C\n"
            f"Feels like: {feels_like}°C\n"
            f"Humidity: {humidity}%\n"
            f"Wind Speed: {wind_speed} m/s\n"
            f"Description: {weather_desc.capitalize()}"
        )
    else:
        weather_report = "City not found or API limit exceeded."
    
    return weather_report

if __name__ == "__main__":
    api_key = "8098db27c11f35e0dedb1d1dfbc95d01c"
    city = input("Enter city name: ")
    print(get_weather(city, api_key))
