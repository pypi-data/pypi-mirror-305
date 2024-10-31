DEFAULT_GOAL := help
PROJECT=crashstats_tools

.PHONY: help
help:
	@echo "Available rules:"
	@echo ""
	@fgrep -h "##" Makefile | fgrep -v fgrep | sed 's/\(.*\):.*##/\1:/'

.PHONY: clean
clean:  ## Clean build artifacts
	rm -rf build dist src/${PROJECT}.egg-info .tox .pytest_cache/
	rm -rf docs/_build/*
	find src tests/ -name __pycache__ | xargs rm -rf
	find src tests/ -name '*.pyc' | xargs rm -rf

.PHONY: format
format:  ## Format files
	tox exec -e py39-lint -- ruff format

.PHONY: lint
lint:  ## Lint files
	tox -e py39-lint

.PHONY: test
test:  ## Run tests
	tox

.PHONY: docs
docs:  ## Update README with fresh cog output
	tox exec -e py38-lint -- cog -r README.rst
