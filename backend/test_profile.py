import requests

url = "http://127.0.0.1:5000/api/profile"

profile = {
    "age": 20,
    "fitness_level": "beginner",
    "goal": "fitness",
    "available_time": 10,
    "movement_type": "seated",
    "equipment": "none"
}

response = requests.post(url, json=profile)

print(response.status_code)
print(response.json())