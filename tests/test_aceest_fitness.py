import pytest
from src.app import app,tracker

@pytest.fixture
def client():
    """
    Provides a test client for the Flask app.
    """
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_homepage_loads(client):
    """
    Ensure the homepage loads successfully with the correct content.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert b"Workouts" in response.data


def test_add_workout_success(client):
    """
    Test adding a valid workout through POST request.
    """
    response = client.post("/add", data={"workout": "Running", "duration": "30"}, follow_redirects=True)
    assert response.status_code in (200,201)
    assert any(w["workout"] == "Running" and w["duration"] == 30 for w in tracker.get_workouts())


def test_add_workout_missing_fields(client):
    """
    Test when workout or duration is missing.
    """
    response = client.post("/add", data={"workout": "", "duration": ""}, follow_redirects=True)
    assert response.status_code == 400


def test_add_workout_invalid_duration(client):
    """
    Test when duration is not a number.
    """
    response = client.post("/add", data={"workout": "Cycling", "duration": "abc"}, follow_redirects=True)
    assert response.status_code == 400


def test_view_workouts(client):
    """
    Test that workouts are displayed correctly after adding.
    """
    tracker.workouts.clear()  # reset state before testing
    tracker.add_workout("Yoga", 45)
    tracker.add_workout("Swimming", 60)

    response = client.get("/")
    assert response.status_code == 200
    assert b"Yoga" in response.data
    assert b"Swimming" in response.data
