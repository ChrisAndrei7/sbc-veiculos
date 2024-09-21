#!/bin/bash
echo "Creating Migrations..."
python manage.py makemigrations pacientes
echo ====================================

echo "Starting Migrations..."
python manage.py migrate
echo ====================================

echo "Starting Server..."
python manage.py runserver 0.0.0.0:8003
