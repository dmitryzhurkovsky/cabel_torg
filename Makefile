.EXPORT_ALL_VARIABLES:
PROD_COMPOSE_FILE ?= docker-compose.yaml
DEV_COMPOSE_FILE ?= docker-compose.dev.yaml

docker-up-dev:  ## Run dev container
	docker-compose -f $(DEV_COMPOSE_FILE) up

docker-build-dev: ## Build dev container
	docker-compose -f $(DEV_COMPOSE_FILE) build

docker-up:  ## Run prod container
	docker-compose -f $(PROD_COMPOSE_FILE) up -d

docker-build: ## Build prod container
	docker-compose -f $(PROD_COMPOSE_FILE) build

migrate-up: ## Run migrations using alembic
	docker-compose -f $(DEV_COMPOSE_FILE) exec backend alembic upgrade head

migrate-down: ## Rollback migrations using alembic
	docker-compose -f $(DEV_COMPOSE_FILE) exec backend alembic downgrade -1

migrate-create: ## Create migrations using alembic
	docker-compose -f $(DEV_COMPOSE_FILE) exec backend alembic revision --autogenerate -m "$(m)"

test: ## Run tests
	docker exec -i backend-test pytest src/tests/.