# Archivo: backend/notas/serializers.py

# --- 1. IMPORTACIONES ---

# 'from rest_framework import serializers'
# Importa la "caja de herramientas" de Serializers (los traductores) de DRF.
from rest_framework import serializers

# 'from .models import Nota'
# Importa nuestro "molde" Nota.
from .models import Nota


# --- 2. TRADUCTOR PARA LA NOTA ---

# 'class NotaSerializer(serializers.ModelSerializer):'
# Creamos un traductor llamado 'NotaSerializer'.
# 'serializers.ModelSerializer' es un traductor "mágico" conectado a un molde de Django.
class NotaSerializer(serializers.ModelSerializer):
    
    # 'class Meta:'
    # La configuración interna del traductor.
    class Meta:
        # 'model = Nota'
        # Le dice al traductor: "Estás conectado al molde 'Nota'".
        model = Nota
        
        # 'fields = '__all__''
        # Le dice al traductor: "Incluye todos los campos de la Nota en el JSON".
        # (id, titulo, contenido, completada, fecha_creacion, fecha_actualizacion).
        fields = '__all__'
        
        # 'read_only_fields = [...]'
        # Define qué campos del JSON SOLO pueden ser leídos (GET),
        # pero NO pueden ser modificados por React (POST, PUT, PATCH).
        # (Las fechas las maneja Django automáticamente, no React).
        read_only_fields = ('fecha_creacion', 'fecha_actualizacion')