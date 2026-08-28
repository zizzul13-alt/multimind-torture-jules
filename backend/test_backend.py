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
    token_sum = sum(m["tokens"] for m in data["messages"])
    assert data["total_tokens"] == token_sum

def test_unsupported_action():
    res = client.post("/api/session/action", json={
        "action_type": "invalid_action_name",
        "payload": {}
    })
    # Pydantic validation returns 422 for unallowed Literal types
    assert res.status_code in [400, 422]

def test_send_message_action():
    res = client.post("/api/session/action", json={
        "action_type": "send_message",
        "payload": {"text": "Testing verified message injection"}
    })
    assert res.status_code == 200
    assert res.json()["success"] is True
    assert len(res.json()["updated_session"]["messages"]) >= 26
