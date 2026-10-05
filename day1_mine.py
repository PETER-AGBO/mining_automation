
equipment = {
    "name": "Crusher",
    "operating_hour": 18,
    "production": 150,
    "status": "Running",
    "maintenance_required": True             
}

print(equipment["name"])
print(equipment["operating_hour"])
print(equipment["production"])

production = 150
operating_hour = 18

throughput = production / operating_hour
print(throughput, "tonnes/hour")

equipment = {
    "name": "Ball Mill",
    "operating_hour": 18,
    "production": 900,
    "status": "Running", 
    "maintenance_required": False           
}

print(equipment["name"])
print(equipment["operating_hour"])
print(equipment["production"])

production = 900
operating_hour = 18

throughput = production / operating_hour
print(throughput, "tonnes/hour")


equipment = {
    "name": "Conveyor",
    "operating_hour": 18,
    "production": 1350,
    "status": "Running",
    "maintenance_required": True          
}

print(equipment["name"])
print(equipment["operating_hour"])
print(equipment["production"])

production = 1350
operating_hour = 18

throughput = production / operating_hour
print(throughput, "tonnes/hour")

