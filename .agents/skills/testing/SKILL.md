---
name: testing
description: How to run the project's validation gates and interpret failures.
---

# Testing

## Execution
Run all tests via:
```bash
pytest -v
```

## Interpreting Failures

Since this is a validation project for a specific Agnara version, an unexpected failure might reflect an actual framework bug or limitation in `0.1.0a8`. 

If a test fails because of a missing feature in `agnara-http==0.1.0a8`:
1. Do **not** invent a mock to hide it.
2. Rewrite the test to assert the actual limitation (e.g. `assert response.status_code == 500`).
3. Document the limitation in `README.md` and `docs/public-api-boundary.md`.
