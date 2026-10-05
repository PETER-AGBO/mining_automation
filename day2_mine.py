# CRUSHER

Crusher = {
   "operating_hour": 18,
   "production": 150,
   "status": "Running",
   "maintenance_required": True
}

print("Crusher")
throughput = Crusher["production"] / Crusher["operating_hour"]
print(throughput, "tonnes/hour")


if Crusher["maintenance_required"]:
    print("Maintenance Required!")
else: 
    print("Equipment is OK.")
    

if throughput >= 50:
    print("Excellent")
elif throughput >= 30:
    print("Good")
elif throughput >= 20:
    print("Acceptable")
else:
    print("Production performance is below target")
    
if Crusher["maintenance_required"] or throughput < 20:
    print("ATTENTION REQUIRED")
else:
    print("NORMAL")   

# BALL MILL    

Ball_Mill = {
    "operating_hour": 18,
    "production": 150,
    "status": "Running",
    "maintenance_required": False
}

print("Ball Mill")
throughput = Ball_Mill["production"] / Ball_Mill["operating_hour"]
print(throughput, "tonnes/hour")

if Ball_Mill["maintenance_required"]:
    print("Maintenance Required!")
else: 
    print("Equipment is OK.")
    

if throughput >= 50:
    print("Excellent")
elif throughput >= 30:
    print("Good")
elif throughput >= 20:
    print("Acceptable")
else:
    print("Production performance is below target")
    

if Ball_Mill["maintenance_required"] or throughput < 20:
    print("ATTENTION REQUIRED")
else:
    print("NORMAL")   


# CONVEYOR

Conveyor = {
    "operating_hour": 18,
    "production": 150,
    "status": "Running",
    "maintenance_required": True
}

print("Conveyor")
throughput = Conveyor["production"] / Conveyor["operating_hour"]
print(throughput, "tonnes/hour")


if Conveyor["maintenance_required"]:
    print("Maintenance Required!")
else: 
    print("Equipment is OK.")
    
    
if throughput >= 50:
    print("Excellent")
elif throughput >= 30:
    print("Good")
elif throughput >= 20:
    print("Acceptable")
else:
    print("Production performance is below target")
    
    
if Conveyor["maintenance_required"] or throughput < 20:
    print("ATTENTION REQUIRED")
else:
    print("NORMAL")
