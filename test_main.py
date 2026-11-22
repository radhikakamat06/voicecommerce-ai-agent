
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_home_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["project"] == "VoiceCommerce AI"


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_existing_order():
    response = client.get("/orders/VC1002")
    assert response.status_code == 200
    assert response.json()["status"] == "Processing"


def test_unknown_order():
    response = client.get("/orders/VC9999")
    assert response.status_code == 404


def test_escalation_endpoint():
    response = client.post(
        "/escalations",
        json={
            "order_id": "VC1002",
            "reason": "refund_dispute",
            "customer_message": "I need help with my refund.",
        },
    )
    assert response.status_code == 200
    assert response.json()["ticket_id"].startswith("VC-")

def test_cancellation_requires_confirmation():
    response = client.post(
        "/orders/VC1002/cancel?confirmed=false"
    )

    assert response.status_code == 200
    assert response.json()["confirmation_required"] is True


def test_cannot_cancel_order_out_for_delivery():
    response = client.post(
        "/orders/VC1001/cancel?confirmed=true"
    )

    assert response.status_code == 200
    assert response.json()["success"] is False
    assert "cannot be cancelled" in response.json()["message"]


def test_can_cancel_eligible_order_after_confirmation():
    response = client.post(
        "/orders/VC1002/cancel?confirmed=true"
    )

    assert response.status_code == 200
    assert response.json()["success"] is True
    assert response.json()["status"] == "Cancelled"
