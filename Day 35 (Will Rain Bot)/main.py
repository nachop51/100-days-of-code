import os
import requests
from twilio.rest import Client

MY_LAT = -34.774830  # YOUR LATITUDE
MY_LON = -55.840389  # YOUR LONGITUDE
API_KEY = "YOUR API KEY HERE"
account_sid = 'ACCOUNT SID HERE'
auth_token = 'TOKEN HERE'

params = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

response = requests.get(
    "https://api.openweathermap.org/data/2.5/onecall", params)

response.raise_for_status()

data = response.json()["hourly"][:12]

will_rain = False

for hour_data in data:
    if hour_data["weather"][0]["id"] < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='whatsapp: NUMBER HERE',
        body="It's going to rain today, Remember to bring an ☂",
        to='whatsapp: NUMBER HERE'
    )
    print(message.sid)
    print(message.status)
