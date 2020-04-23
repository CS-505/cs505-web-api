siddhi.start: ## Start siddhi in its docker container
	docker-compose up siddhi

siddhi.daemon: ## Start daemon siddhi in its docker container
	docker-compose up -d siddhi