Crusher = {
    "name": "Crusher",
    "operating_hour": 18,
    "production": 150,
    "status": "Running",
    "maintenance_required": True
}

Ball_Mill = {
    "name": "Ball Mill",
    "operating_hour": 18,
    "production": 900,
    "status": "Running",
    "maintenance_required": False,
    
}

Conveyor = {
    "name": "Conveyor",
    "operating_hour": 18,
    "production": 1350,
    "status": "Running",
    "maintenance_required": True
}

equipment_count = 0

equipment_list = [Crusher, Ball_Mill, Conveyor]

for equipment in equipment_list:
    print("Name:", equipment["name"])
    
    throughput = equipment["production"] / equipment["operating_hour"]
    print("Throughput:", throughput, "t/hr")
    
    
    if equipment["maintenance_required"]:
        print("Maintenance Required!")
    else:
        print("Equipment is OK.")
        
        
    if throughput >= 50:
        print("Performance:", "Excellent")
    elif throughput >= 30:
        print("Performance:", "Good")
    elif throughput >= 20:
        print("Performance:", "Acceptable")
    else:
        print("Performance:", "Below target")
    
    
    if equipment["maintenance_required"] or throughput < 20:
          print("ATTENTION REQUIRED")
    else:
          print("NORMAL")

    equipment_count +=1

print("Total equipment checked:", equipment_count)