import requests
from datetime import datetime

MY_LAT = -34.774830
MY_LONG = -55.840390


def utc(time):
    time = f"{(int(time) - 3):02}"
    return time


param = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=param)
response.raise_for_status()

data = response.json()

sunrise = utc(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = utc(data["results"]["sunset"].split("T")[1].split(":")[0])

print(sunrise)
print(sunset)
time_now = datetime.now()
print(time_now)
