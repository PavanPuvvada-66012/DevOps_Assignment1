# src/tracker.py

class WorkoutTracker:
    """
    Core logic for tracking workouts (separated from GUI).
    """

    def __init__(self):
        self.workouts = []

    def add_workout(self, workout: str, duration: int) -> dict:
        if not workout or duration is None:
            raise ValueError("Workout and duration are required")

        if not isinstance(duration, int):
            raise ValueError("Duration must be an integer")

        entry = {"workout": workout, "duration": duration}
        self.workouts.append(entry)
        return entry

    def get_workouts(self):
        return self.workouts

