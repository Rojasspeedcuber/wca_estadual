# Base image
FROM python:3.12-slim

# Working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files
COPY . .
COPY original_data.json data.json

# Make the entrypoint script executable
RUN chmod +x entrypoint.sh

# Expose the server port
EXPOSE 8080
ENV API_CLIENT_ID=wca_client_id
ENV API_CLIENT_SECRET=wca_client_secret

# Use the entrypoint script to start both the API and the data generator
ENTRYPOINT ["./entrypoint.sh"]