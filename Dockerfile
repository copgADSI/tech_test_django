# Usa Python 3.10
FROM python:3.10-slim

# Evita bytecode y habilita salida sin buffer
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Directorio de trabajo
WORKDIR /code

# Instalación de dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código y el entrypoint
COPY . .
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Arranque
ENTRYPOINT ["/entrypoint.sh"]
CMD ["gunicorn", "tech_test_django.wsgi:application", "--bind", "0.0.0.0:8000"]
