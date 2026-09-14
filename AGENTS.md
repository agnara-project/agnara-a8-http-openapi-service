# Autonomous Agents Guide

This document is the operational source of truth for autonomous coding agents (such as OpenAI Codex, Claude Code, Google Antigravity, and other compatible systems) interacting with this repository. 

**Audience:** Machine maintainers and autonomous agents. (Human maintainers should refer to `README.md`).

## 1. Project Identity

- **Repository:** `agnara-a8-http-openapi-service`
- **Organization:** `agnara-project`
- **Purpose:** Validate and demonstrate the HTTP/OpenAPI layer of Agnara `0.1.0a8` using `agnara-http`. 
- **Target Agnara Version:** `0.1.0a8` (STRICT)
- **Python Version:** `>=3.14`
- **Status:** Release Validation / Functional
- **Mission:** Prove that a real application can be built entirely on Agnara capabilities and exposed through HTTP bindings, OpenAPI generation, and discovery, without turning HTTP routes into the domain center, and strictly using public 0.1.0a8 APIs.

## 2. Inviolable Architectural Constraints

- **Version Lock:** You must **never** upgrade the `agnara` or `agnara-http` dependency past `0.1.0a8`. This repository exists specifically to validate this snapshot.
- **Dependency Source:** You must **never** use Git references, local paths, or unreleased branches for Agnara dependencies. They must be resolved from PyPI.
- **Public API Strictness:** You must **never** use monkey patches, internal private APIs (starting with `_`), or frameworks outside the public API of Agnara `0.1.0a8`. 
- **No Semantic Frameworks:** Do **not** introduce FastAPI, Flask, or Django as the semantic or domain layer. The domain is built on Agnara Capabilities.
- **Speculation:** Do **not** invent future APIs, document unsupported endpoints, or simulate APIs that are missing. If an API is missing, document it honestly as a limitation.

## 3. Codebase Structure and Ownership

- `src/app/domain.py`: Domain entities utilizing pure Python `dataclasses` (or Pydantic if explicitly needed).
- `src/app/capabilities.py`: Core logic defined as Agnara capabilities (`@app.capability()`).
- `src/app/policies.py`: Security and authorization policies.
- `src/app/server.py`: The HTTP adapter layer, mapping capabilities to ASGI using `agnara_http.Http` and configuring `OpenApiInfo`.
- `tests/test_api.py`: ASGI integration tests over `httpx`.
- `docs/`: Technical reference and specific implementation guidelines.
- `.agents/skills/`: Procedural knowledge and routines specifically tailored for agents working on this repo.

## 4. Environment and Command Palette

Agents must use the following commands to validate the repository from a clean clone:

**Environment & Setup:**
```bash
py -3.14 -m venv .venv
.venv\Scripts\python -m pip install --upgrade pip
.venv\Scripts\pip install -e .[dev]
```

**Quality Gates:**
```bash
.venv\Scripts\ruff format .
.venv\Scripts\ruff check .
.venv\Scripts\pytest -v
```

**Build Validation:**
```bash
.venv\Scripts\python -m build
.venv\Scripts\python -m pip check
```

**Execution (Interactive):**
```bash
.venv\Scripts\python main.py
```

**Docker Smoke Tests:**
```bash
docker compose config
docker compose down --remove-orphans
docker compose build --no-cache
docker compose up -d
docker compose ps
# Verify Endpoints:
curl --fail http://localhost:8000/openapi.json
curl --fail http://localhost:8080/
curl --fail http://localhost:8080/openapi.json
docker compose down --remove-orphans
```

## 5. Public API / Integration Boundary

**Allowed:**
- `agnara.App`, `agnara.Agnara`
- `agnara.execution.Failure`, `agnara.execution.FailureCode`
- `agnara.ScopePolicy`
- `agnara_http.Http`, `agnara_http.Binding`, `agnara_http.BindingSource`
- `agnara_http.OpenApiInfo`, `agnara_http.OpenApiOperation`
- Standard Python 3.14 features (e.g. `dataclasses`).

**Prohibited:**
- Any `agnara._*` internal imports.
- `FastAPI`, `Flask`

## 6. Negative Constraints

- **DO NOT** suppress failing tests merely to make CI green.
- **DO NOT** add SEO filler or speculative content.
- **DO NOT** alter architectural boundaries (e.g. moving business logic into the HTTP routing layer).
- **DO NOT** invent missing Swagger UI routes natively. **Swagger UI is strictly deployment-side**.
- **DO NOT** expose the Docker API strictly to 127.0.0.1 inside the container; it must listen on `0.0.0.0` to route correctly.
- **DO NOT** leak Docker DNS names to the browser. Swagger consumes `/openapi.json` via a same-origin proxy.
- **DO NOT** enable Swagger "Try It Out" by default.

## 7. Git and Contribution Protocol

- **Branching Model:** Feature branching `feature/` or `fix/` -> `main`. 
- **Commits:** Strict adherence to Conventional Commits (`feat:`, `fix:`, `docs:`, `test:`, `refactor:`, `chore:`).

## 8. Documentation Synchronization Contract

If you modify bindings, dependencies, or behavior, you MUST update:
- `README.md`
- `AGENTS.md` (if tools or commands change)
- `ARCHITECTURE.md`
- Relevant files in `docs/`

## 9. Definition of Done

You may consider a task complete only when:
1. All quality gates pass (`ruff format --check`, `ruff check`, `pytest`).
2. Code correctly utilizes Agnara `0.1.0a8` without workarounds.
3. Documentation exactly matches reality.
4. Working tree is clean of unintentional artifacts (`.pytest_cache`, logs, etc).
