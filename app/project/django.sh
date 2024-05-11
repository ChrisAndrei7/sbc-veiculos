#!/bin/bash
echo "Creating Migrations..."
python manage.py makemigrations pedidos
echo ====================================

echo "Starting Migrations..."
python manage.py migrate
echo ====================================

echo "Starting Server..."
python manage.py runserver ec2-54-198-132-244.compute-1.amazonaws.com:8000
