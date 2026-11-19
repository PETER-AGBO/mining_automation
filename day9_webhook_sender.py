import requests

#webhook reciever address
url = "http://127.0.0.1:5000/webhook"

#Simulated mining alert 
alert = {
    "equipment": "Ball Mill",
    "throughput": 50
}

#Send alert to the flask
response = requests.post(url, json=alert)

print("Status Code:", response.status_code)

try: 
    print("Server Response:", response.json())
except requests.exceptions.JSONDecodeError:
    print("Server returned a non-JSON response:")
    print(response.text)