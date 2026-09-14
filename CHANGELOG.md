# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.1] - 2026-09-13
### Added
- Complete Docker validation stack with multi-stage build.
- Deployment-side Swagger UI sidecar proxying natively generated OpenAPI schema.
- Extended OpenAPI contract testing.
- `docs/DOCKER.md` documentation covering topology and Swagger reverse proxying.

## [1.0.0] - 2026-09-13
### Added
- Complete implementation of the HTTP reference service using `agnara==0.1.0a8`.
- Core capabilities for order management (`create`, `get`, `cancel`).
- ASGI compilation mapping with `agnara-http`.
- Test suite validating expected 400 and 403 mappings based on Domain models. (Note: 404 NOT_FOUND is returned by the capability, but unauthenticated HTTP requests correctly halt at 403 Forbidden due to policy constraints. Supplying a Principal natively over HTTP is not part of the `0.1.0a8` public API validation scope).
- Native `/openapi.json` generation.
- Full organizational standardization across governance documents.
- `agnara-http` integration to compile endpoints directly to ASGI 3.
- Native path, query, and body bindings.
- OpenAPI JSON schema generation.
- Full agent-ready documentation including `AGENTS.md` and `ARCHITECTURE.md`.
- Automated testing suite verifying 400 (Validation), 403 (Policy), and 200 (Success) responses.
