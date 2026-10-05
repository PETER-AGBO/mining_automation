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

equipment_list = [Crusher, Ball_Mill, Conveyor]


def calculate_throughput(production, operating_hour):
    return production / operating_hour




def classify_performance(throughput):
    

    if throughput >= 50:
        return "Excellent"
    elif throughput >= 30:
        return "Good"
    elif throughput >= 20:
        return "Acceptable"
    else:
        return "Below target"
    


def determine_status(maintenance_required, throughput):
    
    if maintenance_required  or throughput < 20:
        return "ATTENTION REQUIRED!"
    else:
        return "NORMAL"


# Checking Equipment


def check_equipment(equipment):
    
    throughput = calculate_throughput(
        equipment["production"], 
        equipment["operating_hour"]
    )
    
    performance = classify_performance(throughput)
    
    status = determine_status(
        equipment["maintenance_required"],
        throughput
    )
    
    return throughput, performance, status

for equipment in equipment_list:
    result = check_equipment(equipment)
    print(result)


