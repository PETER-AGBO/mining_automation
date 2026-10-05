import json

with open("mining_equipment.json", "r") as file:
    data = json.load(file)
    
    
  
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
        return "Below Target"
    



def determine_status(maintenance_required, throughput):
    if maintenance_required or throughput < 20:
        return "Attention Required!"
    else:
        return "Normal"
    



# Checking equipment

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
  
  
     
for equipment in data:
   
    result = check_equipment(equipment)
    throughput, performance, status = check_equipment(equipment)
    
    print("Equipment:", equipment["name"])
    print("Throughput:", round(throughput, 2), "t/hr")
    print("Performance:", performance)
    print("Status:", status)
    print()
    