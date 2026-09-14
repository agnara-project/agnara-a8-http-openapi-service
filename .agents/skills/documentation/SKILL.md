---
name: documentation
description: How documentation is structured and kept in sync.
---

# Documentation Sync

This project follows a 4-layer documentation strategy:

1. **Human Introduction (`README.md`)**: The entry point. Explains the "what" and "why". Must always contain accurate execution commands.
2. **Architecture (`ARCHITECTURE.md`, `docs/`)**: Deep dive into components. Modify when structural logic or data flow changes.
3. **Agent Operations (`AGENTS.md`, `.agents/`)**: Machine-readable rules. Must be updated if the command palette, environment constraints, or boundaries change.
4. **Governance (`CONTRIBUTING.md`, `SECURITY.md`, etc.)**: Maintenance rules.

**Rule:** Every PR that modifies bindings, dependencies, or behavior MUST update the corresponding documentation in the exact same commit.
