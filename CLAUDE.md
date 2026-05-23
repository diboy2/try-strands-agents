# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Status

This repository is in its initial state — only `README.md`, `LICENSE`, and `.gitignore` are committed. There is no source code, dependency manifest, build system, or test suite yet. The stated intent (per `README.md`) is to experiment with the Strands agent framework.

When real code is added, this file should be updated with the actual commands and architecture. Do not invent commands or structure before they exist.

## Language & Tooling

The `.gitignore` is Python-flavored (covers `__pycache__`, `.venv`, pytest, mypy, ruff, uv, poetry, pdm, pipenv, Marimo, Streamlit). Assume Python is the target language until proven otherwise. The specific package manager and test runner have not been chosen yet — check for `pyproject.toml`, `requirements.txt`, `uv.lock`, or `poetry.lock` before assuming.
