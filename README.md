# mmcp

Simple CLI client for experimenting with MCP (Model Context Protocol) tool calls over HTTP.

## Quick Start
1. Ensure Python 3.11 is available (see `.python-version`).
2. Install the `uv` tool: follow https://docs.astral.sh/uv/.
3. Sync dependencies:
   ```bash
   uv sync
   ```

## CLI Usage
Inspect available commands:
```bash
uv run python main.py --help
```
List tools exposed by an MCP server:
```bash
uv run python main.py list_tools --host 127.0.0.1 --port 23456
```
Call a specific tool with optional property overrides:
```bash
uv run python main.py call --host 127.0.0.1 --port 23456 \
  --tool example_tool --params '{"query": "value"}' \
  --property response_format=json
```

## Development Workflow
- Lint: `uvx ruff check .`
- Format: `uvx ruff format`
- Type-check: `uvx pyright`
- Run all tests: `uv run pytest`
- Run a single test: `uv run pytest tests/test_file.py::TestClass::test_case`

## Project Notes
- Organize imports as stdlib / third-party / local with blank lines.
- Prefer explicit, typed APIs and async-friendly flows.
- Raise `click.ClickException` for validation errors; allow unexpected errors to surface after logging.
- Avoid adding new dependencies without prior agreement; verify `uv run python main.py list-tools` still works after changes.

## Contributing
Please update this README when flows or commands change and add tests for new features located under `tests/`.
