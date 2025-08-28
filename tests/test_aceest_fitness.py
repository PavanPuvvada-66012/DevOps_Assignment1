"""
Pytest file created to test acceest_fitness App
"""
import tkinter as tk
from unittest.mock import patch
import pytest
from src.aceest_fitness import FitnessTrackerApp


@pytest.fixture
def app(): # pylint: disable=redefined-outer-name
    """
    This function creates a hidden Tkinter root window, initializes your FitnessTrackerApp with it, returns it for use in tests, and then destroys the root window when tests are done.
    """
    root = tk.Tk()
    root.withdraw()
    app = FitnessTrackerApp(root)  # pylint: disable=redefined-outer-name
    yield app   
    root.destroy()


def test_add_workout_success(app): # pylint: disable=redefined-outer-name
    """
    Adding test data to check on the App taking inputs. 
    """
    app.workout_entry.insert(0, "Push Ups")
    app.duration_entry.insert(0, "15")

    with patch("src.accest_fitness.messagebox.showinfo") as mock_info:
        app.add_workout()

    assert len(app.workouts) == 1
    assert app.workouts[0]["workout"] == "Push Ups"
    assert app.workouts[0]["duration"] == 15
    mock_info.assert_called_once()
