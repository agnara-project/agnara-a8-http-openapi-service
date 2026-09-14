import pytest
from playwright.sync_api import Page, expect

def test_swagger_ui_loads(page: Page):
    """
    Validates that Swagger UI renders the Agnara OpenAPI 3.2.0 document correctly.
    This test runs against the live Docker Compose environment at http://localhost:8080.
    """
    try:
        response = page.goto("http://localhost:8080", timeout=10000)
    except Exception as e:
        pytest.skip(f"Swagger UI not reachable at localhost:8080. Is Docker running? {e}")
        
    assert response.status == 200
    
    # Wait for the Swagger UI to load the API definition
    page.wait_for_selector(".swagger-ui", state="visible", timeout=5000)
    
    # Verify the API title is displayed
    title = page.locator(".info")
    expect(title).to_contain_text("Orders API")
    
    # Verify an expected operation is visible
    op = page.locator(".opblock").first
    expect(op).to_be_visible()
    
    # Ensure there are no "Unable to render this definition" errors
    errors = page.locator(".errors-wrapper")
    expect(errors).not_to_be_visible()
