
# Sample order data for our VoiceCommerce AI prototype.
# All customer and order details below are fictional.

ORDERS = {
    "VC1001": {
        "customer_name": "Ananya",
        "status": "Out for delivery",
        "estimated_delivery": "Today, 6 PM - 8 PM",
        "item": "Wireless headphones",
        "cancellable": False,
    },
    "VC1002": {
        "customer_name": "Rahul",
        "status": "Processing",
        "estimated_delivery": "Tomorrow",
        "item": "Running shoes",
        "cancellable": True,
    },
    "VC1003": {
        "customer_name": "Priya",
        "status": "Delivered",
        "estimated_delivery": "Delivered yesterday",
        "item": "Coffee maker",
        "cancellable": False,
    },
}


def get_order(order_id: str):
    """Return order details if the order exists."""
    return ORDERS.get(order_id.upper())
