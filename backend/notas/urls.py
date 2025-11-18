# Archivo: backend/notas/urls.py (¡CORREGIDO!)

# --- 1. IMPORTACIONES ---
# ¡Agregamos 'path'!
from django.urls import path, include 

# 'from rest_framework.routers import DefaultRouter'
from rest_framework.routers import DefaultRouter

# 'from . import views'
from . import views

# --- 2. CONFIGURACIÓN DEL ENRUTADOR AUTOMÁTICO ---

router = DefaultRouter()

# 'router.register(...)'
router.register(r'notas', views.NotaViewSet, basename='nota')


# --- 3. LISTA DE DIRECCIONES (URLS) ---
# La función 'path' ya está importada y lista para usarse.
urlpatterns = [
    # path('', include(router.urls)), <-- Esta línea usa 'include'
    path('', include(router.urls)),
]