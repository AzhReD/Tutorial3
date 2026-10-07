import requests

url = "http://localhost:8000/prediction-batch"
payload = {
    "features": [
        [5.1, 3.5, 1.4, 0.2],
        [6.7, 3.0, 5.2, 2.3]
    ]
}

response = requests.post(url, json=payload)
print("Risposta batch:", response.json())