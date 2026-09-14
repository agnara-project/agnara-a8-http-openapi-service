# Agnara 0.1.0a8 HTTP & OpenAPI Service

A validation project exclusively for Agnara 0.1.0a8.

## Objective

Demonstrate and validate a real HTTP application built on Agnara capabilities, using an Order API scenario (`get`, `create`, `cancel`). This validates the `agnara-http` adapter, ASGI 3 compilation, path/query/body bindings, and OpenAPI generation.

## Project Structure

- `src/app/domain.py`: Domain models using Python dataclasses.
- `src/app/capabilities.py`: Core capabilities definition.
- `src/app/server.py`: HTTP bindings and ASGI compilation.
- `tests/test_api.py`: ASGI tests with HTTPX.

## Execution

1. Create a virtual environment using Python 3.14.
2. Install the dependencies:
   ```bash
   pip install -e .[dev]
   ```
3. Run the ASGI server:
   ```bash
   python main.py
   ```

## Release validation

**Version**: `0.1.0a8`

**Installed Packages**:
- `agnara==0.1.0a8`
- `agnara-http==0.1.0a8`

**Reproducible Commands**:
```bash
py -3.14 -m venv .venv
.venv\Scripts\pip install agnara==0.1.0a8 agnara-http==0.1.0a8 pydantic pytest pytest-asyncio httpx uvicorn
.venv\Scripts\pytest tests/test_api.py -v
```

**Findings & Limitations**:
- **Python 3.14 requirement**: Agnara `0.1.0a8` strictly requires Python >= 3.14.
- **Validations & Dataclasses**: Native `dataclasses` work transparently for bindings. Missing fields correctly raise canonical `INVALID_INPUT` failures represented as `400 Bad Request` in HTTP.
- **Policies**: Applying `scopes=["orders:read"]` at the capability level flawlessly propagates to the HTTP layer, returning a canonical `403 Forbidden` (`{"code": "forbidden"}`) when accessed without proper context.
- **Failures**: Canonical failures such as `Failure(FailureCode.NOT_FOUND, ...)` natively map to their corresponding HTTP status codes (404) without raising exceptions.
- **OpenAPI**: OpenApi dynamically maps capability bindings and is fully generated at `/openapi.json`. We had to explicitly pass `OpenApiOperation(summary=...)` for the operations to populate properly in the schema mapping.
- **Docs UI**: There is no publicly known route for a UI (Swagger/Redoc) activated by default in 0.1.0a8 without additional configuration, only the raw OpenAPI schema at `/openapi.json`.