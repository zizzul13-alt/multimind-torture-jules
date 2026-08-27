import pytest
from starlette.testclient import TestClient
from app import app

client = TestClient(app)

def test_routes_render():
    response = client.get("/ref/arknights")
    assert response.status_code == 200
    assert "PROJECT ARK-MULTIMIND" in response.text

    response = client.get("/ref/noomo")
    assert response.status_code == 200
    assert "FLUID" in response.text

    response = client.get("/ref/dioriviera")
    assert response.status_code == 200
    assert "DIORIVIERA" in response.text

    response = client.get("/ref/viensla")
    assert response.status_code == 200
    assert "TYPOGRAPHY AS ARCHITECTURE" in response.text

def test_multimind_and_mutation():
    response = client.get("/multimind")
    assert response.status_code == 200
    assert "TACTICAL OPS SURFACE" in response.text

    # Test Live Presentation Mutation (POST /mutate-presentation?to=editorial)
    response_mut = client.post("/mutate-presentation?to=editorial")
    assert response_mut.status_code == 200
    assert "MULTIMIND ATELIER" in response_mut.text
    assert "Dr. Aris Thorne" in response_mut.text

    # Check back to tactical
    response_mut2 = client.post("/mutate-presentation?to=tactical")
    assert response_mut2.status_code == 200
    assert "TACTICAL OPS SURFACE" in response_mut2.text

if __name__ == '__main__':
    pytest.main(["-v", "test_app_routes.py"])
