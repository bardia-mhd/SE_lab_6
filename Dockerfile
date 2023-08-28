# Dockerfile

# Base image
FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Set environment variable for SQLite database file
# ENV DATABASE_URL=sqlite:///crud.db

CMD ["python", "app.py"]