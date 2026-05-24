# CLAUDE.md

Guidance for Claude Code (claude.ai/code) working in this repository.

## Project intent

Sandbox for experimenting with the [Strands](https://strandsagents.com) agent framework against a local Ollama backend. Not a library or service — just small, runnable demo scripts under `src/`.

## Tooling

- Python ≥ 3.10, managed by [`uv`](https://docs.astral.sh/uv/) (`pyproject.toml`, `uv.lock`).
- Dependencies: `strands-agents[ollama]`, `strands-agents-builder`, `strands-agents-tools`. Dev group: `mypy`.
- mypy runs in `strict` mode over `src/` with `ignore_missing_imports` for `strands.*` and `strands_tools.*`. See `[tool.mypy]` in `pyproject.toml` for the canonical config — don't duplicate it here.
- Runtime dependency: a local Ollama server at `http://localhost:11434` with the `qwen3:latest` model pulled. Each demo hardcodes that host and model.

## Commands

```bash
uv sync                              # install deps (incl. dev group)
uv run mypy                          # strict type check over src/
uv run python src/agent.py           # run a specific demo
```

## Module map (`src/`)

- `agent.py` — synchronous `Agent` with `calculator`, `current_time`, and a custom `letter_counter` `@tool`. Runs one prompt and prints `result.metrics.get_summary()`.
- `async_agent.py` — async streaming via `agent.stream_async(...)`, with `callback_handler=None` to suppress the default printer. Only tool is `calculator`.
- `callback_agent.py` — custom synchronous `callback_handler(**kwargs)` that logs streamed `data` and `current_tool_use` events via `logging.Logger("my_agent")`. Tool is `shell`.
- `__init__.py` — imports `agent` and `async_agent` only.

## Known quirks (read before editing)

- Each demo runs an agent invocation at module top level — there is no `if __name__ == "__main__":` guard. Importing the module triggers a real LLM call against Ollama. This includes `import src`, since `src/__init__.py` imports two of the three demos.
- `src/__init__.py` deliberately or accidentally omits `callback_agent`. Don't "fix" this without checking intent — adding it would make `import src` invoke the `shell` tool.
- `qwen3:latest` is pinned in every demo because smaller Ollama-hosted models (tested: `llama3.1:8b`, `llama3.2:3b`, `qwen2.5-coder:3b`) return tool calls as text in the `content` field rather than the structured `tool_calls` field, which breaks Strands' tool loop.
