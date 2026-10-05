from app import app

def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.data == b"OK"


def test_add_feedback():
    client = app.test_client()

    response = client.post(
        "/items",
        json={
            "name": "Raj",
            "message": "Good service",
            "rating": 5
        }
    )

    assert response.status_code == 201
    data = response.get_json()

    assert data["name"] == "Raj"
    assert data["message"] == "Good service"
    assert data["rating"] == 5