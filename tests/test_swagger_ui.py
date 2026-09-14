import pytest
from playwright.sync_api import Page, expect


@pytest.mark.docker
def test_swagger_ui_loads(page: Page):
    """
    Validates that Swagger UI renders the Agnara OpenAPI 3.2.0 document correctly.
    This test runs against the live Docker Compose environment at http://localhost:8080.
    """
    response = page.goto("http://localhost:8080", timeout=10000)

    assert response.status == 200

    # Wait for the Swagger UI to load the API definition
    page.wait_for_selector(".swagger-ui", state="visible", timeout=5000)

    # Verify the API title is displayed
    title = page.locator(".info")
    expect(title).to_contain_text("Orders API")

    # Verify expected operations are visible
    expect(page.locator(".opblock-post", has_text="/orders").first).to_be_visible()
    expect(page.locator(".opblock-get", has_text="/orders/{order_id}").first).to_be_visible()
    expect(page.locator(".opblock-delete", has_text="/orders/{order_id}").first).to_be_visible()

    # Ensure there are no "Unable to render this definition" errors
    errors = page.locator(".errors-wrapper")
    expect(errors).not_to_be_visible()
    
    # Check explicitly for "Unable to render this definition" string
    expect(page.locator("body")).not_to_contain_text("Unable to render this definition")
    expect(page.locator("body")).not_to_contain_text("Supported versions are")
