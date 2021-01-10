.DEFAULT_GOAL := help
.PHONY: help build test

IMAGE_NAME := 'openaip3-codegen'
DOCKER_REPOSITORY := 'manchenkoff/${IMAGE_NAME}'
PROJECT_DIRECTORY := $(PWD)

build: ## Build an application
	@pipenv run python setup.py sdist bdist_wheel

publish-test: ## Upload package to test PyPI
	@pipenv run twine upload --repository testpypi dist/*

publish: build ## Upload package to PyPI
	@pipenv run twine upload dist/*
	@make clean

install: build ## Install application to Pip environment
	@pipenv run python setup.py install

install-dev: ## Install application to Pip development environment
	@pipenv run python setup.py develop
	@make clean

clean: ## Remove build files
	@rm -Rf build/ dist/ *.egg-info .pytest_cache/ .mypy_cache/ .pytype/ .eggs/ src/*.egg-info
	@echo "Temporary files were clear"

test: ## Run code tests
	@pipenv run python -m pytest -q

sync: ## Sync with Pipfile packages list
	@pipenv sync

lint: ## Run code linters (mypy / pytype)
	@pipenv run mypy ./src

docker-build: ## Build Docker image
	@docker build . -t ${DOCKER_REPOSITORY} -f docker/Dockerfile

docker-publish: ## Publish image to the Docker Hub
	@docker push ${DOCKER_REPOSITORY}:latest

docker-run: ## Run application in Docker container
	@echo "Work in progress..." # TODO: run image

help: ## Show this message
	@echo "Application management"
	@echo
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'