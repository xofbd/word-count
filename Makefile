POETRY_RUN := poetry run
SHELL := /bin/bash

.PHONY: all
all: clean install

# Installing
.make.install: poetry.lock
	poetry install --no-dev
	rm -f .make.install-dev
	touch $@

.PHONY: install
install: .make.install

.make.install-dev: poetry.lock
	poetry install
	rm -f .make.install
	touch $@

.PHONY: install-dev
install-dev: .make.install-dev

# Virtual environment
poetry.lock: pyproject.toml
	poetry lock
	touch $@

# Testing
.PHONY: test-lint
test-lint: | .make.install-dev
	$(POETRY_RUN) flake8 --config=pyproject.toml src tests

.PHONY: test-unit
test-unit: | .make.install-dev
	$(POETRY_RUN) pytest -s

.PHONY: tests
tests: test-lint test-unit

# Utilities
.PHONY: clean
clean:
	find . | grep [py]cache | xargs rm -rf
	rm -f .make.*

