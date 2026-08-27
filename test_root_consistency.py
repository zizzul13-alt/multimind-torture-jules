import pytest
from starlette.testclient import TestClient
from app import app

client = TestClient(app)

def test_root_and_multimind_consistency():
    res_root = client.get("/")
    assert res_root.status_code == 200
    assert 'id="multimind-app-container"' in res_root.text

    res_mm = client.get("/multimind")
    assert res_mm.status_code == 200
    assert 'id="multimind-app-container"' in res_mm.text

if __name__ == "__main__":
    pytest.main(["-v", "test_root_consistency.py"])
