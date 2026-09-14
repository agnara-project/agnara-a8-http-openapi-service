# Agnara 0.1.0a8 HTTP & OpenAPI Service

A validation project exclusively for Agnara 0.1.0a8 demonstrating a real HTTP application built on capabilities.

## Mission

This repository exists separately from Agnara Core to prove that a real application can be built entirely on Agnara capabilities and exposed through HTTP bindings, OpenAPI generation, and discovery, without turning HTTP routes into the domain center, and strictly using public 0.1.0a8 APIs. It validates the capability abstraction against real-world ASGI deployment realities.

## Scope

**In Scope:**
- Compiling an `agnara.App` into an ASGI 3 application.
- Mapping native Python dataclasses through path, body, and query bindings.
- Executing scope policies natively and propagating HTTP 403.
- Returning canonical `Failure` types that map to standard HTTP errors (e.g. 404, 400).
- Generating OpenAPI JSON definitions natively.

**Out of Scope:**
- Semantic HTTP Frameworks (e.g. FastAPI, Flask). The application is purely Agnara.
- Database access. State is held in-memory to isolate validation to the Agnara-HTTP integration layer.
- Generating Swagger UI endpoints (`agnara-http==0.1.0a8` does not natively serve this by default).

## Release / Compatibility Baseline

- **Agnara Version:** `0.1.0a8`
- **agnara-http Version:** `0.1.0a8`
- **Python Version:** `3.14` (Strict minimum)
- **Status:** Release Validation / Functional

## Prerequisites

- Python 3.14
- Standard shell

## Quick Start

```bash
# Clone and setup environment
git clone https://github.com/agnara-project/agnara-a8-http-openapi-service.git
cd agnara-a8-http-openapi-service
py -3.14 -m venv .venv

# Activate and install dependencies
.venv\Scripts\python -m pip install -e .[dev]

# Run the validation server
.venv\Scripts\python main.py
```

## Usage / Demonstration

While the server runs, you can execute operations against the capabilities:

```bash
# 1. Fetch OpenAPI definition
curl http://127.0.0.1:8000/openapi.json

# 2. Create an order (No scopes required)
curl -X POST "http://127.0.0.1:8000/orders?customer_id=alice" \
     -H "Content-Type: application/json" \
     -d '{"amount": 100, "currency": "USD"}'

# 3. Fetch an order (Fails with 403 because it requires orders:read scope)
curl http://127.0.0.1:8000/orders/1
```

## Conceptual Flow

The application executes in three strict tiers: HTTP Layer -> Capability Layer -> Domain Layer. 
For deep implementation details, see [ARCHITECTURE.md](ARCHITECTURE.md).

## Project Structure

- `src/app/domain.py`: Domain entity contracts (dataclasses).
- `src/app/capabilities.py`: Semantic capabilities defining business rules and policies.
- `src/app/server.py`: The HTTP adapter that compiles capabilities to ASGI and bounds variables.
- `tests/test_api.py`: Automated tests verifying failure mapping and policy execution.
- `docs/`: Technical reference and specific HTTP guides.

## Testing and Verification

To validate that your local environment behaves identically:
```bash
# Code Quality
ruff format --check .
ruff check .

# API Tests
pytest -v

# Package constraints
python -m build
python -m pip check
```

## Known Limitations

- **Docs UI**: There is no publicly known route for a UI (Swagger/Redoc) activated by default in 0.1.0a8 without additional configuration, only the raw OpenAPI schema at `/openapi.json`. We do not mock this feature to maintain an honest benchmark.

## Relationship to Agnara

This is a **point-in-time validation project** belonging to the `agnara-project` ecosystem, frozen to Agnara version `0.1.0a8`. It ensures that subsequent developments do not invalidate the foundational capability integrations built into this release.

## Governance

- **Contributing**: Read [CONTRIBUTING.md](CONTRIBUTING.md) for branch models and PR guidelines.
- **Security**: Security policies are documented in [SECURITY.md](SECURITY.md).
- **Agents**: Autonomous AI Agents must read [AGENTS.md](AGENTS.md) before modifying this repository.
- **License**: Apache 2.0. See [LICENSE](LICENSE).