import httpx
import pytest

from app.server import app


@pytest.mark.asyncio
async def test_openapi():
    async with httpx.AsyncClient(
        transport=httpx.ASGITransport(app=app), base_url="http://test"
    ) as client:
        r = await client.get("/openapi.json")
        assert r.status_code == 200
        data = r.json()
        assert isinstance(data, dict)

        # Version and Info
        assert data["openapi"] == "3.2.0"
        assert data["info"]["title"] == "Orders API"
        assert data["info"]["version"] == "1.0.0"

        # Paths
        paths = data["paths"]
        assert len(paths) == 2, "Accidental unrelated routes present"
        assert "/orders" in paths
        assert "/orders/{order_id}" in paths

        # Methods
        assert "post" in paths["/orders"]
        assert "get" in paths["/orders/{order_id}"]
        assert "delete" in paths["/orders/{order_id}"]

        # Required Path Parameters
        get_op = paths["/orders/{order_id}"]["get"]
        path_params = [p for p in get_op["parameters"] if p["in"] == "path"]
        assert len(path_params) == 1
        assert path_params[0]["name"] == "order_id"
        assert path_params[0]["required"] is True

        # Request body schema
        post_op = paths["/orders"]["post"]
        req_body = post_op["requestBody"]["content"]["application/json"]["schema"]
        assert req_body["type"] == "object"
        assert "amount" in req_body["properties"]
        assert "currency" in req_body["properties"]

        # Documented response codes
        assert "200" in post_op["responses"]
        assert "204" in post_op["responses"]
        assert "default" in post_op["responses"]

        # Operation IDs
        assert post_op["operationId"] == "orders.create_order:post:/orders"


@pytest.mark.asyncio
async def test_create_order():
    async with httpx.AsyncClient(
        transport=httpx.ASGITransport(app=app), base_url="http://test"
    ) as client:
        # Test validation error (amount <= 0)
        r = await client.post("/orders?customer_id=alice", json={"amount": -10, "currency": "USD"})
        assert r.status_code == 400
        assert r.json()["code"] == "invalid_input"

        # Test missing query parameter (customer_id)
        # agnara_http might raise 400 for missing bindings
        r2 = await client.post("/orders", json={"amount": 100, "currency": "USD"})
        assert r2.status_code == 400

        # Test success
        r3 = await client.post("/orders?customer_id=bob", json={"amount": 100, "currency": "USD"})
        assert r3.status_code == 200
        data = r3.json()
        assert data["id"] == "1"
        assert data["status"] == "created for bob"


@pytest.mark.asyncio
async def test_policies_and_not_found():
    async with httpx.AsyncClient(
        transport=httpx.ASGITransport(app=app), base_url="http://test"
    ) as client:
        # GET order requires scopes -> 403 Forbidden
        r = await client.get("/orders/1")
        assert r.status_code == 403
        assert r.json()["code"] == "forbidden"

        # DELETE order requires scopes -> 403 Forbidden
        r2 = await client.request("DELETE", "/orders/1", json={"reason": "test"})
        assert r2.status_code == 403
