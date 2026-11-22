
from datetime import datetime, timezone
from uuid import uuid4


def create_escalation(
    order_id: str,
    reason: str,
    customer_message: str,
):
    """Create a sample human-support escalation ticket."""

    return {
        "ticket_id": f"VC-{uuid4().hex[:8].upper()}",
        "order_id": order_id.upper(),
        "reason": reason,
        "customer_message": customer_message,
        "status": "Open",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "message": (
            "Your request has been flagged for human support. "
            "This prototype has created a sample ticket; "
            "no real support team has been contacted."
        ),
    }
