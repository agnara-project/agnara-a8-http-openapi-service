import agnara
from agnara.execution import Failure, FailureCode

from .domain import CancelReason, OrderCreate, OrderResponse

orders_app = agnara.App("orders")

_orders: dict[str, OrderResponse] = {}
_next_id = 1


# No scopes for create, just to demonstrate successful HTTP bindings
@orders_app.capability()
async def create_order(order: OrderCreate, customer_id: str) -> OrderResponse | Failure:
    if order.amount <= 0:
        return Failure(FailureCode.INVALID_INPUT, "Amount must be positive")
    if not customer_id:
        return Failure(FailureCode.INVALID_INPUT, "Customer ID is required")

    global _next_id
    order_id = str(_next_id)
    _next_id += 1

    new_order = OrderResponse(
        id=order_id,
        amount=order.amount,
        currency=order.currency,
        status=f"created for {customer_id}",
    )
    _orders[order_id] = new_order
    return new_order


# Requires scopes, will fail with 403 if no Principal is provided
@orders_app.capability(scopes=["orders:read"])
async def get_order(order_id: str) -> OrderResponse | Failure:
    if order_id not in _orders:
        return Failure(FailureCode.NOT_FOUND, f"Order {order_id} not found")
    return _orders[order_id]


# Requires scopes, will fail with 403
@orders_app.capability(scopes=["orders:write"])
async def cancel_order(order_id: str, reason: CancelReason) -> OrderResponse | Failure:
    if order_id not in _orders:
        return Failure(FailureCode.NOT_FOUND, f"Order {order_id} not found")

    if len(reason.reason) < 3:
        return Failure(FailureCode.INVALID_INPUT, "Reason too short")

    order = _orders[order_id]
    order.status = f"cancelled: {reason.reason}"
    return order
