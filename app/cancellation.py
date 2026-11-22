
from app.orders import get_order


def cancel_order(order_id: str, confirmed: bool = False):
    """Cancel an eligible order only after customer confirmation."""

    order = get_order(order_id)

    if order is None:
        return {
            "success": False,
            "message": "Order not found. Please check the order ID.",
        }

    if not order["cancellable"]:
        return {
            "success": False,
            "message": (
                f"Sorry, your order is currently "
                f"'{order['status']}' and cannot be cancelled."
            ),
        }

    if not confirmed:
        return {
            "success": False,
            "confirmation_required": True,
            "message": (
                f"Your order for {order['item']} is eligible "
                "for cancellation. Do you want to proceed?"
            ),
        }

    order["status"] = "Cancelled"
    order["cancellable"] = False

    return {
        "success": True,
        "order_id": order_id.upper(),
        "status": order["status"],
        "message": "Your order has been cancelled successfully.",
    }
