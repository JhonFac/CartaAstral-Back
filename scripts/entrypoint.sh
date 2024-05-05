#!/bin/sh

set -e
# start Container
echo "Contenedor iniciado"
echo "$(date): Ejecutando proceso"

# Obtener la dirección IP interna del contenedor
CONTAINER_IP=$(hostname -I | awk '{print $1}')

echo "La dirección IP del contenedor es: $CONTAINER_IP"

python manage.py collectsatic
python manage.py makemigrations
python manage.py migrate
# python manage.py runserver 0.0.0.0:8000
python manage.py runserver 0.0.0.0:$PORT



