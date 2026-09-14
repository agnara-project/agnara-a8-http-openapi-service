# HTTP Binding Validation Guide

This document records the exact syntax used to bind Agnara capabilities to HTTP requests in `agnara-http` version `0.1.0a8`.

## 1. Setup

Import the necessary classes from `agnara_http`.
```python
from agnara_http import Http, Binding, BindingSource, OpenApiInfo, OpenApiOperation
```

## 2. Path Bindings
Used for injecting URL variables into capability arguments.
```python
http.get("/orders/{order_id}", get_order, Binding("order_id", BindingSource.PATH))
```

## 3. Body Bindings
Extracts a JSON payload into a dataclass or model.
```python
http.post("/orders", create_order, Binding("order", BindingSource.BODY))
```

## 4. Query Bindings
Extracts a query parameter (`?customer_id=123`).
```python
http.post(
    "/orders",
    create_order,
    # Can be combined with Body bindings for multiple arguments
    Binding("customer_id", BindingSource.QUERY),
)
```

## 5. Exposing OpenAPI

To generate OpenAPI definitions natively, pass `openapi=OpenApiInfo(...)` to `compile`, and annotate routes with `OpenApiOperation(...)`.

```python
http.get(
    "/orders/{order_id}",
    get_order,
    Binding("order_id", BindingSource.PATH),
    openapi=OpenApiOperation(summary="Get an order"),
)

asgi_app = http.compile(
    frozen, openapi=OpenApiInfo(title="Orders API", version="1.0.0"), openapi_path="/openapi.json"
)
```
