from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api_produccion.urls')),  # Incluye las URLs de tu aplicación api_producciones
]
