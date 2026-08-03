#!/bin/sh
set -e

# Create database tables if they don't exist
python create_db.py

# Start the data generator in the background
python data_generator.py &
DATA_GENERATOR_PID=$!

# Trap signals to gracefully stop the data generator when the container stops
trap 'kill -TERM $DATA_GENERATOR_PID 2>/dev/null || true' TERM INT

# Start the Flask API server in the foreground
exec gunicorn -b 0.0.0.0:8080 api:app
