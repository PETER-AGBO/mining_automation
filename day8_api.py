import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos")

data = response.json()

equipment_data = [
    {
        "name": "Crusher",
        "production": 150,
        "operating_hour": 18
    },
    {
        "name": "Ball Mill",
        "production": 900,
        "operating_hour": 18
    },
    {
        "name": "Conveyor",
        "production": 1350,
        "operating_hour": 18
    }
]


for equipment in equipment_data:
    
    
    throughput = equipment["production"] / equipment["operating_hour"]
    print(equipment["name"], round(throughput, 2), "t/hr")