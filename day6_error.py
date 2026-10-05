import json

with open("mining_equipment.json", "r") as file:
    data = json.load(file)
    
    
  
def calculate_throughput(production, operating_hour):
    try:
        return production / operating_hour
    except ZeroDivisionError:
        print("Error:", "Invalid operating hour.")
        return None


def classify_performance(throughput):
    if throughput >= 50:
        return "Excellent"
    elif throughput >= 30:
        return "Good"
    elif throughput >= 20:
        return "Acceptable"
    else: 
        return "Below Target"
    



def determine_status(maintenance_required, throughput):
    if maintenance_required or throughput < 20:
        return "Attention Required!"
    else:
        return "Normal"
    



# Checking equipment

def check_equipment(equipment):
    try:
        production = equipment["production"]
        operating_hour = equipment["operating_hour"]
        maintenance_required = equipment["maintenance_required"]
        
        throughput = production / operating_hour
        
    except KeyError:
        return None, None, None, "Production data missing"
    except ZeroDivisionError:
        return None, None, None, "Invalid operating hours"
        
    
    performance = classify_performance(throughput)
    
    status = determine_status(maintenance_required, throughput)

    return throughput, performance, status, None
  
  
     
for equipment in data:
    throughput, performance, status, error = check_equipment(equipment)
    
    print("Equipment:", equipment["name"])
    if error:
        print("⚠️ Error:", error)
    else:
        throughput, performance, status, error 
        print("Throughput:", round(throughput, 2), "t/hr")
        print("Performance:", performance)
        print("Status:", status)
    print()
    