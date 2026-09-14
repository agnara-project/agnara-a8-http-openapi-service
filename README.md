# Agnara 0.1.0a8 HTTP & OpenAPI Service

A validation project exclusively for Agnara 0.1.0a8 demonstrating a real HTTP application built on capabilities.

## Project Identity

This is the frozen validation and reference service for:
* Agnara `0.1.0a8`
* `agnara-http` `0.1.0a8`
* HTTP composition
* Native OpenAPI generation
* Dockerized Swagger visualization

## Status

**FINAL/FROZEN**: This project is final validation infrastructure, not a moving example following future Agnara versions. It strictly validates what can be achieved by a consumer of the published public 0.1.0a8 API.

## Architecture

* **Application Architecture**: Domain → Capabilities → Agnara application → agnara-http → ASGI → OpenAPI
* **Visualization Architecture**: OpenAPI → Docker Swagger UI sidecar

The application purely uses Agnara capabilities. Swagger UI acts exclusively as a deployment visualization layer and is **not a private Agnara import**. This respects the strict public API boundary of 0.1.0a8. For more details see [ARCHITECTURE.md](ARCHITECTURE.md).

## Local Python Quick Start

For local native development (Windows/Linux):

```bash
# Clone the repository
git clone https://github.com/agnara-project/agnara-a8-http-openapi-service.git
cd agnara-a8-http-openapi-service

# Create virtual environment (Python 3.14 required)
py -3.14 -m venv .venv

# Activate and install dependencies
.venv\Scripts\python -m pip install -e ".[dev]"

# Run the validation server
.venv\Scripts\python main.py
```
*The API will listen at http://127.0.0.1:8000.*

## Docker Quick Start

To deploy the API and its companion Swagger UI in a containerized environment:

```bash
docker compose up --build
```

**Services:**
* **API URL**: `http://localhost:8000`
* **Raw OpenAPI URL**: `http://localhost:8000/openapi.json`
* **Swagger UI URL**: `http://localhost:8080` (Loads the API schema directly without exposing internal Docker networking to your browser).

## Example Requests

While the API runs locally or on Docker, execute:

```bash
# Fetch OpenAPI definition
curl http://localhost:8000/openapi.json

# Create an order (No scopes required)
curl -X POST "http://localhost:8000/orders?customer_id=alice" -H "Content-Type: application/json" -d "{\"amount\": 100, \"currency\": \"USD\"}"

# Fetch an order (Fails with 403 because it requires orders:read scope)
curl http://localhost:8000/orders/1
```

## Repository Role

This repository specifically validates how to construct an ASGI service over `agnara==0.1.0a8`. 

**Note on Swagger UI:**
* OpenAPI lo genera Agnara.
* Swagger UI solamente lo visualiza.
* Swagger no forma parte de la API pública de `agnara-http==0.1.0a8`.
* Por eso este repositorio usa un contenedor Swagger separado.
* Esto cambiará solamente en futuros releases de Agnara si Swagger pasa a formar parte de la API pública.

## Limitations

* **No known runtime blockers remain.**

## Quality Gates

To reproduce our continuous integration pipeline locally:

```bash
ruff format --check .
ruff check .
pytest -v
python -m build
python -m pip check
docker compose config
docker compose build --no-cache
docker compose up -d
docker compose ps
docker compose down --remove-orphans
```

## Governance

* **Contributing**: See [CONTRIBUTING.md](CONTRIBUTING.md) for branch models and local tests.
* **Security**: See [SECURITY.md](SECURITY.md) for vulnerability disclosure and Docker threat surface.
* **Agents**: See [AGENTS.md](AGENTS.md) for the automated modification rules constraints.
* **License**: Apache 2.0. See [LICENSE](LICENSE).