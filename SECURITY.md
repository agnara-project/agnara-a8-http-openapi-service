# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |

*Note: This repository validates Agnara 0.1.0a8, but the repository version itself is 1.0.x.*

## Scope

This policy applies specifically to the `agnara-a8-http-openapi-service` repository and its interaction with Agnara `0.1.0a8`.

## Swagger / Docker Threat Surface

This repository includes a deployment-side Swagger UI (`docker-compose.yml`). The following threat model applies:
- **Localhost Only**: Swagger and OpenAPI are published exclusively on `127.0.0.1`. Production deployments must make an explicit decision about exposing API documentation.
- **Same-Origin Constraint**: No Docker DNS names are exposed to the browser. Swagger acts as a proxy to avoid CORS weaknesses. OpenAPI is published locally.
- **Try It Out**: Interactive requests are disabled by default (`SUPPORTED_SUBMIT_METHODS=[]`).
- **Remote Validator**: Disabled by default (`VALIDATOR_URL=none`) to avoid external dependencies.
- **No Secrets**: Documentation and Swagger configuration must never contain embedded credentials or secrets.
- **Hardened Image**: Swagger UI is pinned to an exact version (`v5.32.15`) and runs with container hardening (`no-new-privileges:true`).
- **Intended Usage**: This setup is intended purely as a local/validation tool, not for direct public exposure.

## Reporting a Vulnerability

If you discover a security vulnerability within this project, please report it via a **Private Security Advisory** on GitHub, or email `security@agnara.dev`.

Please **do not** open a public issue for security-related flaws.

## Threat Surface

As a validation repository, this project is designed to run locally or in ephemeral CI environments. However, the architectural validation it provides forms the basis for production applications. 

- Do not commit secrets, tokens, or PII.
- Ensure that testing does not leak local credentials.

## Disclosure

We aim to address vulnerabilities rapidly and will coordinate disclosure appropriately.
