# --- 1. IMPORTACIONES ---

# 'from django.db import models'
# Importa el kit de herramientas principal de Django (ORM)
# que nos permite definir "Modelos" (moldes para las tablas de la base de datos).
from django.db import models

# 'from django.utils import timezone'
# Importa una herramienta de Django que maneja
# fechas y horas de forma correcta y consciente de la zona horaria.
from django.utils import timezone


# --- 2. MOLDE: LA NOTA ---

# 'class Nota(models.Model):'
# Esta línea DEFINE nuestro "molde" principal llamado 'Nota'.
# Al heredar de 'models.Model', Django sabe que debe crear
# una tabla en la base de datos (se llamará 'notas_nota').
class Nota(models.Model):
    
    # 'titulo = models.CharField(max_length=200)'
    # Crea la columna para el TÍTULO de la nota.
    # 'models.CharField' -> Significa que la columna guarda TEXTO CORTO (string).
    # 'max_length=200' -> Regla: el título no puede exceder 200 caracteres.
    titulo = models.CharField(max_length=200)
    
    # 'contenido = models.TextField()'
    # Crea la columna para el CONTENIDO de la nota.
    # 'models.TextField' -> Significa que guarda TEXTO LARGO.
    contenido = models.TextField()
    
    # 'fecha_creacion = models.DateTimeField(...)'
    # Crea una columna para guardar la FECHA y HORA de creación.
    # 'default=timezone.now' -> Regla: usa la fecha y hora actual automáticamente al crear la nota.
    fecha_creacion = models.DateTimeField(default=timezone.now)
    
    # 'fecha_actualizacion = models.DateTimeField(...)'
    # Crea una columna para guardar la FECHA y HORA de la última edición.
    # 'auto_now=True' -> Regla: CADA VEZ que se guarda la nota, este campo se actualiza automáticamente.
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    # 'completada = models.BooleanField(...)'
    # Crea una columna para marcar la nota como completada (útil para listas de tareas).
    # 'models.BooleanField' -> Guarda valores TRUE o FALSE (Booleano).
    # 'default=False' -> Regla: por defecto, la nota NO está completada.
    completada = models.BooleanField(default=False)


    # 'def __str__(self):'
    # Esta es una función de Python (NO es una columna de la base de datos).
    # Le dice a Django cómo "nombrar" a una Nota para los humanos (ej: en el Panel de Admin).
    def __str__(self):
        # Muestra el título de la nota.
        return self.titulo
    
    # 'class Meta:'
    # La clase Meta es la configuración interna del modelo.
    class Meta:
        # 'ordering = ['-fecha_creacion']'
        # Regla: Cuando Django traiga la lista de notas, deben estar ordenadas
        # por fecha de creación ('fecha_creacion') de forma descendente ('-').
        # (Esto hace que las notas más nuevas aparezcan primero).
        ordering = ['-fecha_creacion']