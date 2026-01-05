# NXTG-Forge - Makefile

.PHONY: help install dev-install test lint format typecheck security clean build docker-build docker-up docker-down deploy

# Default target
.DEFAULT_GOAL := help

help:  ## Show this help message
	@echo "NXTG-Forge - Development Commands"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install:  ## Install production dependencies
	pip install -r requirements.txt
	npm install

dev-install:  ## Install development dependencies
	pip install -r requirements.txt
	pip install -e ".[dev]"
	npm install
	pre-commit install

test:  ## Run all tests
	pytest tests/ -v --cov=forge --cov-report=term-missing --cov-report=html

test-unit:  ## Run unit tests only
	pytest tests/unit/ -v

test-integration:  ## Run integration tests only
	pytest tests/integration/ -v

test-watch:  ## Run tests in watch mode
	pytest-watch tests/ -v

lint:  ## Run linter (ruff)
	ruff check forge/ tests/

lint-fix:  ## Run linter with auto-fix
	ruff check --fix forge/ tests/

format:  ## Format code with black
	black forge/ tests/
	isort forge/ tests/

format-check:  ## Check code formatting
	black --check forge/ tests/
	isort --check forge/ tests/

typecheck:  ## Run type checker (mypy)
	mypy forge/ --ignore-missing-imports

security:  ## Run security checks
	safety check
	bandit -r forge/ -f json

quality:  ## Run all quality checks
	@echo "Running linter..."
	@make lint
	@echo "\nRunning formatter check..."
	@make format-check
	@echo "\nRunning type checker..."
	@make typecheck
	@echo "\nRunning security checks..."
	@make security

clean:  ## Clean build artifacts and cache
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".ruff_cache" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +
	rm -rf build/ dist/ htmlcov/ .coverage

build:  ## Build Python package
	python -m build

docker-build:  ## Build Docker image
	docker build -t nxtg-forge:latest .

docker-up:  ## Start Docker containers
	docker-compose up -d

docker-down:  ## Stop Docker containers
	docker-compose down

docker-logs:  ## View Docker logs
	docker-compose logs -f

docker-shell:  ## Open shell in Docker container
	docker-compose exec forge bash

status:  ## Show project status
	python forge/cli.py status

checkpoint:  ## Create checkpoint (usage: make checkpoint MSG="description")
	python forge/cli.py checkpoint "$(MSG)"

gap-analysis:  ## Run gap analysis
	python forge/cli.py gap-analysis

health:  ## Show project health score
	python forge/cli.py health

docs:  ## Generate documentation
	@echo "Generating documentation..."
	@echo "See docs/ directory"

deploy:  ## Deploy application (placeholder)
	@echo "Deployment not yet configured"
	@echo "See docs/DEPLOYMENT.md for manual deployment steps"

.PHONY: pre-commit
pre-commit:  ## Run pre-commit hooks on all files
	pre-commit run --all-files

init-dev:  ## Initialize development environment
	@echo "Initializing NXTG-Forge development environment..."
	@make dev-install
	@make format
	@echo "\n✅ Development environment ready!"
	@echo "Run 'make test' to verify installation"
