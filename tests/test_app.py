import sys
from pathlib import Path

sys.path.insert(
    0,
    str(Path(__file__).resolve().parents[1] / "backend")
)

from app import app


def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "OK"


def test_payment():
    client = app.test_client()
    response = client.get("/payment")
    assert response.status_code == 200
    assert response.json["payment_status"] == "SUCCESS"


def test_notification():
    client = app.test_client()
    response = client.get("/notification")
    assert response.status_code == 200
    assert response.json["notification_status"] == "SENT"