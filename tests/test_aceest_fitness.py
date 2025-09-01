"""
Pytest file created to test acceest_fitness App
"""
import tkinter as tk
from unittest.mock import patch
import pytest # pylint: disable=import-error
from src.aceest_fitness import FitnessTrackerApp


@pytest.fixture
def app(): # pylint: disable=redefined-outer-name
    """
    initializes FitnessTrackerApp, 
    returns it for use in tests, and then destroys the root window when tests are done.
    """
    root = tk.Tk()
    root.withdraw()
    app = FitnessTrackerApp(root) # pylint: disable=redefined-outer-name
    yield app
    root.destroy()


def test_add_workout_success(app): # pylint: disable=redefined-outer-name
    """
    Will add a test workout 
    """
    app.workout_entry.insert(0, "Running")
    app.duration_entry.insert(0, "30")

    with patch("tkinter.messagebox.showinfo") as mock_info:
        app.add_workout()

    assert len(app.workouts) == 1
    assert app.workouts[0] == {"workout": "Running", "duration": 30}
    mock_info.assert_called_once_with("Success", "'Running' added successfully!")


def test_add_workout_missing_fields(app): # pylint: disable=redefined-outer-name
    """
    Will add a test workout with empty results
    """
    app.workout_entry.insert(0, "")
    app.duration_entry.insert(0, "")

    with patch("tkinter.messagebox.showerror") as mock_error:
        app.add_workout()

    assert len(app.workouts) == 0
    mock_error.assert_called_once_with("Error", "Please enter both workout and duration.")


def test_add_workout_invalid_duration(app): # pylint: disable=redefined-outer-name
    """
    Will add a test workout with duration in wrong format
    """
    app.workout_entry.insert(0, "Cycling")
    app.duration_entry.insert(0, "abc")

    with patch("tkinter.messagebox.showerror") as mock_error:
        app.add_workout()

    assert len(app.workouts) == 0
    mock_error.assert_called_once_with("Error", "Duration must be a number.")


def test_view_workouts_empty(app): # pylint: disable=redefined-outer-name
    """
    Will check on empty logged workouts
    """
    with patch("tkinter.messagebox.showinfo") as mock_info:
        app.view_workouts()

    mock_info.assert_called_once_with("Workouts", "No workouts logged yet.")


def test_view_workouts_with_data(app): # pylint: disable=redefined-outer-name
    """
    Test to view logged workouts
    """
    app.workouts = [
        {"workout": "Running", "duration": 30},
        {"workout": "Yoga", "duration": 45},
    ]

    with patch("tkinter.messagebox.showinfo") as mock_info:
        app.view_workouts()

    expected_message = (
        "Logged Workouts:\n"
        "1. Running - 30 minutes\n"
        "2. Yoga - 45 minutes\n"
    )
    mock_info.assert_called_once_with("Workouts", expected_message)
