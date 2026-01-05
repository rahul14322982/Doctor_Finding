import requests

url = "https://doctor-finding.onrender.com/predict"

data = {
    "symptoms": symptoms,   # value you already get from HTML
    "address": address
}

headers = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0"
}

response = requests.post(url, json=data, headers=headers)

# get output
status_code = response.status_code
result_text = response.text
