# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /code

# Install system dependencies
RUN apt-get update && apt-get install -y build-essential libpq-dev

# Install pipenv
RUN pip install pipenv

# Copy project files
COPY Pipfile Pipfile.lock ./
RUN pipenv install --deploy --ignore-pipfile

# Copy the entire app
COPY . .

# Expose FastAPI default port
EXPOSE 8000

# Run the application
CMD ["pipenv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
