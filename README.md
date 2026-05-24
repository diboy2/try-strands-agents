# try-strands-agents

Small sandbox for experimenting with the [Strands](https://strandsagents.com) agent framework against a local [Ollama](https://ollama.ai) backend. Three short demos cover the common ways to drive a Strands `Agent`: synchronous tool use, async event streaming, and a custom callback handler.

## Prerequisites

- Python ≥ 3.10
- [`uv`](https://docs.astral.sh/uv/) for environment and dependency management
- A running Ollama server with the `qwen3:latest` model:

  ```bash
  ollama pull qwen3:latest
  ollama serve
  ```

  `qwen3:latest` is used because it reliably emits structured `tool_calls` through Ollama's chat API; smaller models often return tool invocations as plain text and break the agent loop.

## Setup

```bash
uv sync
```

## Run the demos

```bash
uv run python src/agent.py           # sync agent + tools
uv run python src/async_agent.py     # async streaming
uv run python src/callback_agent.py  # custom callback handler
```

## Type check

```bash
uv run mypy
```

## What each demo shows

- **`src/agent.py`** — synchronous `Agent(...)` call with a custom `@tool`-decorated `letter_counter` alongside the community `calculator` and `current_time` tools; prints `result.metrics.get_summary()` after the call.
- **`src/async_agent.py`** — disables the default callback handler and iterates `agent.stream_async(prompt)` to print streamed token chunks and announce tool-use deltas as they arrive.
- **`src/callback_agent.py`** — registers a custom `callback_handler` that routes streamed data and tool-use events to `logging` instead of stdout; uses the `shell` tool to answer "What operating system am I using?".
