# Base image for FastAPI
FROM python:3.8.0

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and set the working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Copy SSL certificate and key files to the container
COPY certfile.pem /app/certfile.pem
COPY keyfile.pem /app/keyfile.pem

# Expose the port FastAPI will run on
EXPOSE 7010

# Command to run the FastAPI application with SSL/TLS
CMD ["uvicorn", "load_balancer:app", "--host", "0.0.0.0", "--port", "7010", "--ssl-keyfile", "/app/keyfile.pem", "--ssl-certfile", "/app/certfile.pem", "--reload"]
