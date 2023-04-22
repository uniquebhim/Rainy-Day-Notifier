import os
import requests
from twilio.rest import Client

# Define the latitude and longitude of your location
MY_LATITUDE = 45.255203
MY_LONGITUDE = 79.843826

# API key for OpenWeatherMap API
WEATHER_API_KEY = "api_key"

# API credentials for Twilio API
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token =  os.environ['TWILIO_AUTH_TOKEN']

# Construct the API request URL with the location and API key as query parameters
weather_api_url = "https://api.openweathermap.org/data/2.5/onecall"
query_params = {
    'lat': MY_LATITUDE,
    'lon': MY_LONGITUDE,
    'appid': WEATHER_API_KEY,
    'exclude': 'current,minutely,daily'
}

# Send the API request and parse the response JSON
response = requests.get(weather_api_url, params=query_params)
response.raise_for_status()
weather_data = response.json()

# Extract the hourly forecast for the next 12 hours
hourly_forecast = weather_data['hourly'][:12]

# Check if it will rain in the next 12 hours
will_rain = any(hour['weather'][0]['id'] < 700 for hour in hourly_forecast)

# If it will rain, send an SMS using the Twilio API
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella.. ☔️",
        from_='+918123456789',
        to='+918123456787'
    )
    print("SMS sent successfully.")
    """
    #important step for envirnment
    1.export TWILIO_ACCOUNT_SID=value_sid
      export TWILIO_AUTH_TOKEN=value_token
            
    2.env
    3.import os
    4.account_sid = os.environ['TWILIO_ACCOUNT_SID']
      auth_token =  os.environ['TWILIO_AUTH_TOKEN']
    
    """
