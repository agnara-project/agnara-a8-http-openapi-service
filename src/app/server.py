import agnara
from agnara_http import Binding, BindingSource, Http, OpenApiInfo, OpenApiOperation

from .capabilities import cancel_order, create_order, get_order, orders_app


def create_asgi_app():
    http = Http()

    # GET /orders/{order_id} -> Path binding
    http.get(
        "/orders/{order_id}",
        get_order,
        Binding("order_id", BindingSource.PATH),
        openapi=OpenApiOperation(summary="Get an order"),
    )

    # POST /orders -> Body + Query binding
    http.post(
        "/orders",
        create_order,
        Binding("order", BindingSource.BODY),
        Binding("customer_id", BindingSource.QUERY),
        openapi=OpenApiOperation(summary="Create a new order"),
    )

    # DELETE /orders/{order_id} -> Path + Body binding
    http.delete(
        "/orders/{order_id}",
        cancel_order,
        Binding("order_id", BindingSource.PATH),
        Binding("reason", BindingSource.BODY),
        openapi=OpenApiOperation(summary="Cancel an order"),
    )

    runtime = agnara.Agnara("order_service")
    runtime.include(orders_app)
    frozen = runtime.compile()

    openapi_info = OpenApiInfo(
        title="Orders API",
        version="1.0.0",
        description="A real HTTP application built on capabilities",
    )

    asgi_app = http.compile(frozen, openapi=openapi_info, openapi_path="/openapi.json")

    return asgi_app


app = create_asgi_app()
