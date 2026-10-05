import json
import logging

logging.basicConfig(level=logging.INFO)


with open("mining_equipment.json", "r") as file:
    data = json.load(file)
    



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
  
total_equipment = 0
successful_equipment = 0
error_count = 0  

logging.info("Mining equipment analysis started.")
     
with open("mining_daily_report.txt", "w") as report:
    report.write("MINING EQUIPMENT DAILY REPORT\n")
    report.write("==============================\n")
    report.write("Date: 2026-10-05\n")
    report.write("\n")
    
    for equipment in data:
        throughput, performance, status, error = check_equipment(equipment)
      
        
        

        total_equipment += 1
    
        print("Equipment:", equipment["name"])
    
   
        if error:
            logging.warning(f"{equipment['name']}: {error}")
            report.write(f"Equipment: {equipment['name']}\n")
            report.write(f"ERROR: {error}\n")
            report.write("\n")
            error_count += 1       
            print("⚠️ Errors:", error)
        else:
            logging.info(f"{equipment['name']}: processed successfully.")
            report.write(f"Equipment: {equipment['name']}\n")
            report.write(f"Throughput: {round(throughput, 2)} t/hr\n")
            report.write(f"Performance: {performance}\n")
            report.write(f"Status: {status}\n")
            report.write("\n")
            successful_equipment += 1
        
    report.write("==============================\n")
    report.write("REPORT SUMMARY\n")
    report.write("==============================\n")
    
    report.write(f"Total Equipment: {total_equipment}\n")
    report.write(f"Successfully Processed: {successful_equipment}\n")
    report.write(f"Errors: {error_count}\n")
