#!/usr/bin/env bash
# Le dice al script que se detenga si un comando falla
set -o errexit

# 1. Instala todas las dependencias
pip install -r requirements.txt

# 2. Recolecta los archivos estáticos (del Admin)
python3 manage.py collectstatic --no-input

# 3. Aplica las migraciones de la base de datos
python3 manage.py migrate

# 4. Crea el superusuario (¡Truco para producción!)
# Usará las variables de entorno que pondremos en Railway
python3 manage.py createsuperuser --no-input || echo "El Superusuario ya existe."