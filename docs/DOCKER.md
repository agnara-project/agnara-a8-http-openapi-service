# Docker & Swagger UI Reference

This document explains the final Docker topology and Swagger visualization design for this `0.1.0a8` validation project.

## Architecture & Topology

The Docker Compose setup creates a self-contained runtime consisting of two services:

1. **`agnara-api` (Port 8000)**
   - The minimal, multi-stage, Python 3.14 container serving the ASGI Agnara App.
   - Listens on `0.0.0.0` internally and exposes `http://127.0.0.1:8000` to the host.
   - Exposes the raw schema natively via `http://localhost:8000/openapi.json`.

2. **`swagger-ui` (Port 8080)**
   - A sidecar container built from the official `swaggerapi/swagger-ui:v5.32.15`.
   - Exposes `http://127.0.0.1:8080` to the host.
   - Acts as a reverse-proxy and frontend. It uses a custom Nginx template (`swagger-nginx.conf`) to serve the UI and route `/openapi.json` to the API container (`http://agnara-api:8000/openapi.json`).

### Why a Sidecar for Swagger?
Agnara `0.1.0a8`'s public API does **not** expose internal Swagger providers natively. Implementing Swagger through Python would require mocking unsupported `agnara-http` functionality or importing private `_` internal packages, both of which violate the strict public API boundary. A sidecar architecture allows Swagger to be a deployment visualizer, natively consuming the valid OpenAPI JSON contract emitted by the `agnara-api` service.

### Same-Origin Schema Proxy
Docker DNS names (like `http://agnara-api:8000`) cannot be embedded directly into browser configuration because desktop browsers do not have access to the Docker internal network DNS. We implement a **same-origin proxy** via Nginx inside the Swagger container. The Swagger frontend queries `/openapi.json`, and Nginx routes that traffic inside the Docker network. This guarantees a seamless developer experience without relying on permissive global CORS.

## Execution

### Startup
To start the services locally:
```bash
docker compose up -d --build
```
*Wait approximately 5 seconds for healthchecks to pass.*

### Health Inspection
```bash
docker compose ps
docker compose logs agnara-api
```

### Shutdown & Clean State
```bash
docker compose down --remove-orphans
# To clean build cache and rebuild from scratch:
docker compose build --no-cache
```

## Security Posture
- **Localhost Bound**: Ports are mapped to `127.0.0.1`, not `0.0.0.0`, preventing exposure to the entire local network.
- **Try-It-Out Disabled**: By default, `SUPPORTED_SUBMIT_METHODS=[]` is passed to the Swagger UI container, disabling interactive submissions from the browser to align with Agnara a8's conservative API exposure design.
- **Non-Root**: `agnara-api` runs as an unprivileged user inside the container.
- **Hardened Capabilities**: Both containers run with `no-new-privileges:true`. `agnara-api` runs with `cap_drop: ALL`.

## Troubleshooting

- **Port already in use**: If port 8000 or 8080 fails to bind, ensure you don't have another service (or python script) running locally on those ports.
- **Swagger loads but schema fails (502 / Connection Refused)**: The `agnara-api` container might be unhealthy or in a restart loop. Inspect logs with `docker compose logs agnara-api`.
- **API container unhealthy**: Check that Uvicorn successfully bound to `0.0.0.0:8000` (controlled by `HOST` and `PORT` environment variables inside the container).
