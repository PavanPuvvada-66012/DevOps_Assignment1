# app.py
"""
Module that client interacts with
"""
from flask import Flask, request, jsonify, render_template
from src.tracker import WorkoutTracker

app = Flask(__name__)
tracker = WorkoutTracker()

"""
Defines routes
"""
@app.route("/")
def home():
    return render_template("index.html", workouts=tracker.get_workouts())

"""
Call functions from the tracker module to maintain the workout list
"""
@app.route("/add", methods=["POST"])
def add_workout():
    data = request.form or request.json
    workout = data.get("workout")
    duration = data.get("duration")

    try:
        duration = int(duration)
        entry = tracker.add_workout(workout, duration)
        return jsonify({"status": "success", "workout": entry}), 201
    except ValueError:
	    return jsonify({"status": "error", "message": "Duration must be an integer"}), 400
"""
To view the workouts details 
"""
@app.route("/workouts", methods=["GET"])
def view_workouts():
    return jsonify(tracker.get_workouts())

if __name__ == "__main__":
    app.run(debug=True)
