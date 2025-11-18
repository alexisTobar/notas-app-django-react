# --- 1. IMPORTACIONES ---

# 'from django.contrib import admin'
# Importa las herramientas del Panel de Administrador de Django.
from django.contrib import admin

# 'from .models import Nota'
# Importa el "molde" Nota que definimos en models.py.
from .models import Nota


# --- 2. CONFIGURACIÓN PERSONALIZADA DEL ADMIN ---

# 'class NotaAdmin(admin.ModelAdmin):'
# Esto crea una configuración avanzada para el formulario de la Nota.
class NotaAdmin(admin.ModelAdmin):
    
    # 'list_display = [...]'
    # Define qué columnas se mostrarán en la *lista* principal del Admin.
    # Así, puedes ver la nota, su estado, y cuándo se actualizó, de un vistazo.
    list_display = ('titulo', 'completada', 'fecha_actualizacion')
    
    # 'list_filter = [...]'
    # Agrega un filtro en el costado derecho para poder filtrar
    # rápidamente por 'Completada' o 'No Completada'.
    list_filter = ('completada',)
    
    # 'fieldsets = [...]'
    # Organiza el formulario de edición de la Nota en secciones legibles.
    fieldsets = [
        ("Información de la Nota", {"fields": ["titulo", "contenido"]}),
        ("Estado y Fechas", {"fields": ["completada", "fecha_creacion", "fecha_actualizacion"]}),
    ]
    
    # 'readonly_fields = [...]'
    # Define qué campos el usuario puede ver, pero NO editar.
    # (Las fechas de creación y actualización deben ser solo de lectura).
    readonly_fields = ('fecha_creacion', 'fecha_actualizacion')


# --- 3. REGISTRANDO EL MODELO ---

# 'admin.site.register(Nota, NotaAdmin)'
# Esta es la orden final. Le dice a Django:
# "Registra el modelo 'Nota', pero usa la configuración
# personalizada 'NotaAdmin' que acabamos de crear".
admin.site.register(Nota, NotaAdmin)