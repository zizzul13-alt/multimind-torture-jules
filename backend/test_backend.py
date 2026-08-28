from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_health():
    res = client.get("/api/health")
    assert res.status_code == 200
    assert res.json()["status"] == "ok"

def test_session():
    res = client.get("/api/session")
    assert res.status_code == 200
    data = res.json()
    assert data["id"] == "session-multimind-torture-01"
    assert len(data["messages"]) >= 25
    assert len(data["agents"]) == 3

def test_morphology_action():
    res = client.post("/api/session/action", json={
        "action_type": "change_morphology",
        "payload": {"morphology": "tactical"}
    })
    assert res.status_code == 200
    assert res.json()["success"] is True
    assert res.json()["updated_session"]["active_morphology"] == "tactical"
