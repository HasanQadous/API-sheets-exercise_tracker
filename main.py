import requests
import datetime
import os

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
Ex_Endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
Sheet_endpoint = os.environ["SHEET_ENDPOINT"]

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0",
}

exercise_text = input("Tell me which exercises you did: ")

parameters = {
 "query": exercise_text,
 "gender": "male",
 "weight_kg": 100,
 "height_cm": 180,
 "age": 24,
}
now = datetime.datetime.now()
current_date = now.strftime("%d/%m/%Y")
time = now.strftime("%X")

ex_response = requests.post(url=Ex_Endpoint, json=parameters, headers=headers)
data = ex_response.json()
print(data)

for exercise in data["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": current_date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

sheet_response = requests.post(url=Sheet_endpoint, json=sheet_inputs)
print(sheet_response.text)

#Basic Authentication
sheet_response = requests.post(
  Sheet_endpoint,
  json=sheet_inputs,
  auth=(
      "hasanqadous",
      "Ha$n1998",
  )
)

#Bearer Token Authentication
bearer_headers = {
    "Authorization": "Bearer YOUR_TOKEN"
}

sheet_response = requests.post(
    Sheet_endpoint,
    json=sheet_inputs,
    headers=bearer_headers
)