import pytest
import httpx
from app.server import app

@pytest.mark.asyncio
async def test_openapi():
    async with httpx.AsyncClient(transport=httpx.ASGITransport(app=app), base_url="http://test") as client:
        r = await client.get("/openapi.json")
        assert r.status_code == 200
        data = r.json()
        assert "openapi" in data
        assert data["info"]["title"] == "Orders API"
        assert "/orders" in data["paths"]

@pytest.mark.asyncio
async def test_create_order():
    async with httpx.AsyncClient(transport=httpx.ASGITransport(app=app), base_url="http://test") as client:
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
    async with httpx.AsyncClient(transport=httpx.ASGITransport(app=app), base_url="http://test") as client:
        # GET order requires scopes -> 403 Forbidden
        r = await client.get("/orders/1")
        assert r.status_code == 403
        assert r.json()["code"] == "forbidden"
        
        # DELETE order requires scopes -> 403 Forbidden
        r2 = await client.request("DELETE", "/orders/1", json={"reason": "test"})
        assert r2.status_code == 403
