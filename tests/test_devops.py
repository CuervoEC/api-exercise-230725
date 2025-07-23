from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

payload = {"message": "This is a test", "to": "Juan Perez", "from": "Rita Asturia", "timeToLifeSec": 45}


def test_post_devops():
    response = client.post("/DevOps", json=payload)
    caller = payload["to"]
    assert response.status_code == 200
    assert response.json()["message"] == f"Hello {caller} your message will be send"


def test_get_devops():
    response = client.get("/DevOps")
    assert response.status_code == 405
    assert response.json()["message"] == "ERROR"


def test_put_devops():
    response = client.put("/DevOps", json=payload)
    assert response.status_code == 405
    assert response.json()["message"] == "ERROR"


def test_patch_devops():
    response = client.patch("/DevOps", json=payload)
    assert response.status_code == 405
    assert response.json()["message"] == "ERROR"


def test_delete_devops():
    response = client.delete("/DevOps")
    assert response.status_code == 405
    assert response.json()["message"] == "ERROR"
