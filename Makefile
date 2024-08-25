CONTAINER_NAME = python-ETL

up:
	docker compose up --build -d

bash: up
	docker exec -it $(CONTAINER_NAME) /bin/bash

down:
	docker-compose down

run:
	$(MAKE) bash