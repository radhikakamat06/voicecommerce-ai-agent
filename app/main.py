
from pathlib import Path
from fastapi.responses import FileResponse
from pydantic import BaseModel
from app.escalation import create_escalation
from fastapi import FastAPI, HTTPException
from app.orders import get_order
from app.cancellation import cancel_order

app = FastAPI(
    title="VoiceCommerce AI",
    description="A multilingual AI voice agent for e-commerce support.",
    version="0.2.0",
)


@app.get("/")
def home():
    return {
        "project": "VoiceCommerce AI",
        "status": "running",
        "message": "Your voice agent backend is ready.",
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.get("/orders/{order_id}")
def order_status(order_id: str):
    order = get_order(order_id)

    if order is None:
        raise HTTPException(
            status_code=404,
            detail="Order not found. Please check the order ID.",
        )

    return {
        "order_id": order_id.upper(),
        **order,
    }

@app.post("/orders/{order_id}/cancel")
def cancel_order_endpoint(order_id: str, confirmed: bool = False):
    result = cancel_order(order_id, confirmed)

    if result.get("message") == "Order not found. Please check the order ID.":
        raise HTTPException(status_code=404, detail=result["message"])

    return result




class EscalationRequest(BaseModel):
    order_id: str
    reason: str
    customer_message: str


@app.post("/escalations")
def escalate_to_human(request: EscalationRequest):
    return create_escalation(
        order_id=request.order_id,
        reason=request.reason,
        customer_message=request.customer_message,
    )
@app.get("/demo", include_in_schema=False)
def demo():
    html_file = Path(__file__).parent / "static" / "index.html"
    return FileResponse(html_file)