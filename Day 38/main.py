import requests
from datetime import datetime
import private  # This is a file that contains your API key
import os

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/d429f6acc8a3b9187e50c74022f477c4/workoutTracking/workouts"

headers = {
    "x-app-id": os.environ['x-app-id-nlq'],
    "x-app-key": os.environ['x-app-key-nlq'],
    "x-remote-user-id": os.environ['x-remote-user-id-nlq'],
}

exercise_parameters = {
    "query": input("Exercises today: "),
    "gender": "male",
    "weight_kg": 77,
    "height_cm": 195,
    "age": 19,
}

sheety_authentication = {
    "Authorization": os.environ['Authorization-nlq']
}

response = requests.post(
    exercise_endpoint,
    headers=headers,
    json=exercise_parameters
)

result = response.json()["exercises"]

for exercise in result:
    sheety_params = {
        "workout": {
            "date": datetime.now().strftime("%d/%m/%Y"),
            "time": datetime.now().strftime("%H:%M:%S"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    response = requests.post(
        sheety_endpoint,
        json=sheety_params,
        headers=sheety_authentication
    )
