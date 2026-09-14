---
name: http-openapi-validation
description: Project-specific skill for validating OpenAPI generation and HTTP bindings in Agnara.
---

# HTTP and OpenAPI Validation

This project validates Agnara's HTTP bindings. When modifying `src/app/server.py`:

1. **Bindings**: Use `agnara_http.Binding` and `agnara_http.BindingSource`. Ensure you cover at least PATH, QUERY, and BODY in any validation scenario.
2. **OpenAPI generation**: Always attach `openapi=OpenApiOperation(summary="...")` to the `http.get`, `http.post` methods so that `/openapi.json` correctly populates metadata.
3. **Docs UI**: Agnara `0.1.0a8` does not expose `/docs`, `/redoc`, or `/swagger` natively. Only `/openapi.json` is exposed. Do not attempt to add UI middleware; it violates the strict boundary condition of testing pure native APIs.
