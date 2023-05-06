#!/bin/bash

# Login to Docker
echo "Logging in to Docker Hub..."
docker login -u yourusername -p yourpassword

# Start the Docker container
echo "Starting the Docker container..."
docker-compose up -d
