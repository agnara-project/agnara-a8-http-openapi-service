---
name: repository-maintenance
description: How an agent should safely inspect, modify, and verify this repository.
---

# Repository Maintenance

This repository strictly validates Agnara 0.1.0a8 HTTP capabilities.

## Safety Rules
1. **Never upgrade Agnara:** `agnara` and `agnara-http` must remain pinned at `0.1.0a8`.
2. **Never mock limitations:** If Agnara 0.1.0a8 lacks a feature, document the failure instead of writing mock code to hide it.
3. **No semantic HTTP frameworks:** Do not add FastAPI or Flask. 

## Modification Workflow
1. Use `ruff format .` and `ruff check .` after modifying Python code.
2. Run `pytest -v` to ensure capability logic remains intact.
3. If public behavior changes, update `README.md` and `docs/public-api-boundary.md`.
