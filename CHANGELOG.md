# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-09-13

### Added
- Initial baseline validating Agnara `0.1.0a8`.
- Order API domain using native `dataclasses`.
- Capabilities layer defining `create_order`, `get_order`, and `cancel_order`.
- Explicit `ScopePolicy` definitions protecting read and write operations.
- `agnara-http` integration to compile endpoints directly to ASGI 3.
- Native path, query, and body bindings.
- OpenAPI JSON schema generation.
- Full agent-ready documentation including `AGENTS.md` and `ARCHITECTURE.md`.
- Automated testing suite verifying 400 (Validation), 403 (Policy), 404 (Canonical Failure), and 200 (Success) responses.
