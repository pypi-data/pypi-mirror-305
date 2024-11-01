install:
	pip install uv
	uv sync

install_dev:
	pip install uv
	uv sync --dev

precommit:
	pre-commit install
	pre-commit run --files $$(git diff --cached --name-only)

test:
	pytest -v

lint:
	black .
	flake8 --exclude .venv --max-line-length 100 .

.PHONY: install install_dev precommit test lint
