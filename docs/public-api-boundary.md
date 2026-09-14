# Public API Boundary Reference

This repository deliberately restricts itself to the public APIs available in Agnara `0.1.0a8`.

## Verified Public Imports

The following APIs have been verified to work and should be used without issue:

**`agnara` Core:**
- `agnara.App`
- `agnara.Agnara`
- `agnara.ScopePolicy`
- `agnara.execution.Failure`
- `agnara.execution.FailureCode`

**`agnara_http` Adapter:**
- `agnara_http.Http`
- `agnara_http.Binding`
- `agnara_http.BindingSource`
- `agnara_http.OpenApiInfo`
- `agnara_http.OpenApiOperation`

## Intentionally Absent APIs

The following APIs are intentionally excluded or do not exist natively:
- No automatic Swagger UI generation (`/docs` or `/swagger`). Only `/openapi.json` is exported.
- No `execute()` on standard capability objects; they are routed through ASGI or `ExecutionPlan`.

## Prohibited Imports

- `agnara._*` (Internal modules)
- `agnara_http._*` (Internal modules)
- `FastAPI`, `Flask`, `Django` (Excluded as they form alternate semantic layers).
