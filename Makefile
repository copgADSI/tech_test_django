.PHONY: build up down migrate logs shell

build:
	docker compose build

up:
	docker compose up -d

down:
	docker compose down

migrate:
	docker compose run --rm web python manage.py migrate

logs:
	docker compose logs -f

shell:
	docker compose run --rm web python manage.py shell
