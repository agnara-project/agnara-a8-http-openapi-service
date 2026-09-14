# Contributing

Thank you for contributing to the Agnara ecosystem! 

This repository specifically validates `0.1.0a8`. 

## Project Status

**Frozen/Validation Only**. This project tests a very specific version of Agnara. We do not accept PRs that upgrade the Agnara dependency or radically change the framework unless coordinating a broader compatibility matrix update.

## Contribution Types Accepted

- **Bug Fixes:** Corrections to the validation application logic or tests.
- **Documentation:** Improvements to `README.md`, `AGENTS.md`, `ARCHITECTURE.md`, etc.
- **CI/CD:** Improvements to GitHub Actions.

## Setup

1. `py -3.14 -m venv .venv`
2. `.venv\Scripts\pip install -e .[dev]`

## Branching & Commits

- Branch from `main` using `feature/<name>`, `fix/<name>`, or `docs/<name>`.
- Use [Conventional Commits](https://www.conventionalcommits.org/). Examples:
  - `feat: add new validation endpoint`
  - `fix: correct typo in openapi config`
  - `docs: clarify architecture`

## Quality Gates

Before opening a PR, ensure all local validations pass:

```bash
# Format and Lint
ruff format --check .
ruff check .

# Tests
pytest -v

# Build Validation
python -m build
python -m pip check

# Docker Smoke Tests
docker compose config
docker compose down --remove-orphans
docker compose build --no-cache
docker compose up -d
curl --fail http://localhost:8000/openapi.json
curl --fail http://localhost:8080/
docker compose down
```

## Pull Request Process

1. Provide a clear description of the change.
2. State why it is necessary.
3. Confirm that tests and documentation have been updated (Documentation Synchronization Contract).
4. Do not alter the core architecture without explicit approval.
