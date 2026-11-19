
from flask import Flask, request, jsonify

# Create a Flask application
app = Flask(__name__)


# Create a webhook endpoint
@app.route("/webhook", methods=["POST"])
def receive_alert():

    # Step 1: Receive incoming JSON data
    alert = request.get_json(silent=True)

    # Step 2: Check whether valid JSON was received
    if alert is None:
        return jsonify({
            "status": "error",
            "message": "No valid JSON data received"
        }), 400

    # Step 3: Ensure incoming data is a dictionary
    if not isinstance(alert, dict):
        return jsonify({
            "status": "error",
            "message": "Expected a JSON object"
        }), 400

    # Step 4: Check for missing fields
    required_fields = ["equipment", "throughput", "target"]

    for field in required_fields:
        if field not in alert:
            return jsonify({
                "status": "error",
                "message": f"{field} is missing"
            }), 400

    # Step 5: Validate equipment name
    if not isinstance(alert["equipment"], str) or not alert["equipment"].strip():
        return jsonify({
            "status": "error",
            "message": "Equipment name must be valid text"
        }), 400

    # Step 6: Validate numeric values
    equipment = alert["equipment"]
    throughput = alert["throughput"]
    target = alert["target"]

    if (isinstance(throughput, bool) or
            not isinstance(throughput, (int, float))):
        return jsonify({
            "status": "error",
            "message": "Throughput must be a number"
        }), 400

    if (isinstance(target, bool) or
            not isinstance(target, (int, float))):
        return jsonify({
            "status": "error",
            "message": "Target throughput must be a number"
        }), 400
        
   
    # Step 7: Validate positive target and non-negative throughput
    if throughput < 0:
        return jsonify({
            "status": "error",
            "message": "Throughput cannot be negative"
        }), 400

    if target <= 0:
        return jsonify({
            "status": "error",
            "message": "Target throughput must be greater than zero"
        }), 400

    # Step 8: Extract validated values
    equipment_name = alert["equipment"]

    # Step 9: Display mining alert
    print("\nMINING ALERT RECEIVED")
    print("Equipment:", equipment_name)
    print("Actual Throughput:", throughput, "t/hr")
    print("Target Throughput:", target, "t/hr")

    # Step 10: Check equipment performance
    if throughput < target:
        print("Status: BELOW TARGET")
        print("Action: Investigate equipment performance.")
    else:
        print("Status: NORMAL")
        print("Action: Continue monitoring.")

    # Step 11: Send successful response
    return jsonify({
        "status": "success",
        "message": "Mining alert received successfully!"
    }), 200


# Start the server
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)




























# from flask import Flask, request, jsonify

# # Create a Flask application
# app = Flask(__name__)

# # Create a webhook endpoint
# @app.route("/webhook", methods=["POST"])
# def receive_alert():

#     # Receive the incoming JSON data
#     # alert = request.get_json()

#   # Recieve incoming JSON data (Handling errors in recievers)
    
#     alert = request.get_json(silent=True)
    
#     if alert is None:
#         return jsonify({
#             "status": "error",
#             "message": "No valid JSON data recieved"
       
#     }), 400
        
#         #Validate throughput data type
    
#     if not isinstance(alert["throughput"], (int, float)):
#         return jsonify({
#             "status": "error",
#             "message": "Throughput must be a number"
#         }), 400
        
#    # Validate target data type
#     if not isinstance(alert["target"], (int, float)):
#         return jsonify({
#             "status": "error",
#             "message": "Target throughput must be a number"
#         }), 400      
       
  
        
#     # Checking if required field exists
        
#     if "equipment" not in alert:
#         return jsonify({
#             "status": "error",
#             "message": "Equipment name is missing"
#         }), 400
        
    
#     if "throughput" not in alert:
#         return jsonify({
#             "status": "error",
#             "message": "Throughput data missing"
#         }), 400
        
    
#     if "target" not in alert:
#         return jsonify({
#             "status": "error",
#             "message": "Target throughput is missing"
#         }), 400

#     # # Display the received alert
#     # print("Received Mining Alert:", alert)
    
#     #Extract values from the alert dictionary
#     equipment_name = alert["equipment"]
#     throughput = alert["throughput"]
#     target = alert["target"]
    
#     # Display the mining equipment
#     print("\nMINING ALERT RECEIVED")
#     print("Equipment:", equipment_name)
#     print("Actual Throughput:", throughput, "t/hr")
#     print("Target Throughput:", target)
    
    

#     # Check equipment performance
#     if throughput < target:
#             print("Status: BELOW TARET")
#             print("Action: Investigate equipment performance.")
#     else:
#             print("Status: NORMAL")
#             print("Action: Continue monitoring.")

#     # Send a successful response to the sender
#     return jsonify({
#         "status": "success",
#         "message": "Mining alert received successfully!"
#     }),200
    


# # Start the server
# if __name__ == "__main__":
#     app.run(host="127.0.0.1", port=5000, debug=True)




