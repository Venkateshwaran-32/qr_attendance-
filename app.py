# Import necessary libraries
from flask import Flask, render_template, request, jsonify  # Flask for routing and handling requests
from sheets_helper import log_to_sheet  # Import the Sheets API integration function
import datetime  # To handle timestamps
from time import time  # To track time in seconds

# Initialize the Flask app
app = Flask(__name__)

# Dictionary to track IP addresses and their last submission time
last_submission = {}

# Home route to display the input form and button
@app.route('/')
def home():
    return render_template('index.html')  # Load the HTML page with the form and button

# Submit route to handle attendance logging
@app.route('/submit', methods=['POST'])
def submit():
    # Extract the user's IP address
    user_ip = request.remote_addr

    # Get the current timestamp in seconds
    current_time = time()

    # Check if this IP has already submitted attendance within the last 60 seconds
    if user_ip in last_submission:
        time_difference = current_time - last_submission[user_ip]
        if time_difference < 600:  # Restrict to one submission per minute
            return jsonify({"error": f"You can only mark attendance again in {int(600 - time_difference)} seconds."}), 429


    # Extract data from the incoming request
    data = request.get_json()
    user_name = data.get('user_name')  # User's name
    user_id = data.get('user_id')      # User's unique ID
    location = data.get('location')    # Latitude and longitude from the frontend
    timestamp = datetime.datetime.now().isoformat()  # Current timestamp

    # Validate inputs
    if not user_name or not user_id:
        return jsonify({"error": "User name and ID are required."}), 400

    # Log the data to Google Sheets
    try:
        log_to_sheet(user_name, user_id, location, timestamp)
        last_submission[user_ip] = current_time  # Record the submission time for this IP
        return jsonify({"message": "Attendance logged successfully!", "timestamp": timestamp})
    except Exception as e:
        print("Error logging to Google Sheets:", e)
        return jsonify({"error": "Failed to log attendance."}), 500

# Run the app in debug mode
if __name__ == "__main__":
    app.run(debug=True)
