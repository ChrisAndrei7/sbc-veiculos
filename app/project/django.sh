#!/bin/bash
echo "Creating Migrations..."
python manage.py makemigrations pedidos
echo ====================================

echo "Starting Migrations..."
python manage.py migrate
echo ====================================

echo "Starting Server..."
python manage.py runserver http://54.198.132.244:8000
