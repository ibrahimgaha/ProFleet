#!/bin/bash

# Render start script for PRO FLEET Django application

echo "Starting PRO FLEET deployment..."

# Run migrations
echo "Running database migrations..."
python manage.py migrate --noinput

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Start Gunicorn server
echo "Starting Gunicorn server..."
gunicorn pro_fleet.wsgi:application --bind 0.0.0.0:$PORT
