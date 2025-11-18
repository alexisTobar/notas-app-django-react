# Archivo: backend/notas/views.py

# --- 1. IMPORTACIONES ---

# 'from rest_framework import viewsets'
# Importamos 'viewsets' (un conjunto de "ventanillas" pre-hechas por DRF).
from rest_framework import viewsets

# 'from .models import Nota'
# Importamos nuestro "molde" Nota.
from .models import Nota

# 'from .serializers import NotaSerializer'
# Importamos nuestro "traductor".
from .serializers import NotaSerializer


# --- 2. VENTANILLA: EL CRUD COMPLETO ---

# 'class NotaViewSet(viewsets.ModelViewSet):'
# Creamos una "ventanilla" para las Notas.
# 'ModelViewSet' es un conjunto pre-hecho por DRF que incluye
# todas las funciones CRUD automáticas:
# - GET /notas/ (LISTAR todas las notas)
# - POST /notas/ (CREAR una nota nueva)
# - GET /notas/1/ (LEER el detalle de una nota)
# - PUT/PATCH /notas/1/ (ACTUALIZAR una nota)
# - DELETE /notas/1/ (BORRAR una nota)
class NotaViewSet(viewsets.ModelViewSet):
    
    # 'queryset = Nota.objects.all()'
    # Esta es la consulta a la base de datos. Le dice a la ventanilla:
    # "Trabaja con TODAS las notas, ordenadas por el Meta.ordering en models.py".
    queryset = Nota.objects.all()
    
    # 'serializer_class = NotaSerializer'
    # Conecta la ventanilla con el traductor.
    # "Usa 'NotaSerializer' para convertir los datos a JSON".
    serializer_class = NotaSerializer