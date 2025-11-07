# Agent Guidelines
1. Use Python 3.11; install deps via `uv sync`.
2. Run the CLI with `uv run python main.py --help` to explore commands.
3. Run linting through `uvx ruff check .`; keep output clean.
4. Format with `uvx ruff format`; do not commit unformatted files.
5. Type-check using `uvx pyright`; address warnings proactively.
6. Execute full tests with `uv run pytest` (add tests under `tests/`).
7. Run a single test via `uv run pytest tests/test_file.py::TestClass::test_case`.
8. Organize imports as stdlib / third-party / local with blank lines.
9. Keep imports explicit; avoid wildcard `*` and unused imports.
10. Prefer type annotations on public functions and dataclasses when modeling payloads.
11. Maintain async-friendly APIs; await coroutines instead of blocking calls.
12. Raise `click.ClickException` for CLI validation errors and provide actionable messages.
13. Let unexpected errors surface after logging context; avoid bare `except`.
14. Use f-strings for formatting and `json.dumps(..., indent=2)` for responses.
15. Keep functions focused; extract helpers for complex flows or repeated parsing.
16. Validate and coerce user input early; ensure CLI params stay typed.
17. Write tests alongside new features; mirror CLI behavior with integration tests.
18. Update `README.md` when commands or flows change.
19. Avoid new dependencies without owner buy-in; confirm `uv run python main.py list-tools` still works.
