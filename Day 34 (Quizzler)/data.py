import requests

params = {
    "amount": 10,
    "type": "boolean",
}

questions = requests.get("https://opentdb.com/api.php", params=params)

question_data = questions.json()

question_data = question_data["results"]
