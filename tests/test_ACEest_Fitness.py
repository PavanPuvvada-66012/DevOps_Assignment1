import pytest
import tkinter as tk
from unittest.mock import patch
from src.aceest_fitness import FitnessTrackerApp


@pytest.fixture
def app():
    root = tk.Tk()
    root.withdraw()
    app = FitnessTrackerApp(root)
    yield app
    root.destroy()


def test_add_workout_success(app):
    app.workout_entry.insert(0, "Push Ups")
    app.duration_entry.insert(0, "15")

    with patch("src.accest_fitness.messagebox.showinfo") as mock_info:
        app.add_workout()

    assert len(app.workouts) == 1
    assert app.workouts[0]["workout"] == "Push Ups"
    assert app.workouts[0]["duration"] == 15
    mock_info.assert_called_once()
