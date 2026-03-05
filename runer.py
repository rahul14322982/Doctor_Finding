import requests
import json

url = "https://doctor-finding.onrender.com/predict"

data = {
    "symptoms": "Fever,Cold",
    "address": "Harihar, Karnataka"
}

response = requests.post(url, json=data)

print("Status code:", response.status_code)
print("Raw response text:")
print(response.text)

# save response to JSON file
with open("output.json", "w", encoding="utf-8") as f:
    f.write(response.text)

print("Data saved to output.json")

