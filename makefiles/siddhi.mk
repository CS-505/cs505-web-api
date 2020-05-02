siddhi.start: ## Start siddhi in its docker container
	docker-compose up --build siddhi-runner

siddhi.dev:
	docker-compose up siddhi

siddhi.daemon: ## Start daemon siddhi in its docker container
	docker-compose up -d --build siddhi-runner