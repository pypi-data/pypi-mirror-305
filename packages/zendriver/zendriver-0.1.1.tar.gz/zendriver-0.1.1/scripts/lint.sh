#!/usr/bin/env bash

set -e
set -x

uv run mypy zendriver
uv run ruff check zendriver
uv run ruff format zendriver --check
