# app.py
from flask import Flask, request, jsonify, render_template
from src.tracker import WorkoutTracker

app = Flask(__name__)
tracker = WorkoutTracker()

@app.route("/")
def home():
    return render_template("index.html", workouts=tracker.get_workouts())

@app.route("/add", methods=["POST"])
def add_workout():
    data = request.form or request.json
    workout = data.get("workout")
    duration = data.get("duration")

    try:
        duration = int(duration)
        entry = tracker.add_workout(workout, duration)
        return jsonify({"status": "success", "workout": entry}), 201
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

@app.route("/workouts", methods=["GET"])
def view_workouts():
    return jsonify(tracker.get_workouts())

if __name__ == "__main__":
    app.run(debug=True)

