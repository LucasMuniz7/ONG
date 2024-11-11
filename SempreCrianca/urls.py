from django.contrib import admin
from django.urls import path, include  # Certifique-se de importar 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),  # Incluindo as URLs do seu app
]
