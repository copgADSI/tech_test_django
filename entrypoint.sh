#!/usr/bin/env bash
set -e

# 1) Espera a Postgres
until pg_isready -h "$POSTGRES_HOST" -p "$POSTGRES_PORT"; do
  echo "Esperando a Postgres..."
  sleep 1
done

# 2) Migraciones y superuser
python manage.py migrate --noinput
python manage.py createsuperuser --noinput || true

# 3) Inicia Gunicorn
exec "$@"
