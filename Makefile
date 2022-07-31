docker-up:  ## Run container
	docker-compose -f docker-compose.dev.yaml up

docker-build: ## Build container
	docker-compose -f docker-compose.dev.yaml build

migrate-up: ## Run migrations using alembic
	docker-compose -f docker-compose.dev.yaml exec backend alembic upgrade head

migrate-down: ## Rollback migrations using alembic
	docker-compose -f docker-compose.dev.yaml exec backend alembic downgrade -1

migrate-create: ## Create migrations using alembic
	docker-compose -f docker-compose.dev.yaml exec backend alembic revision --autogenerate -m "$(m)"
