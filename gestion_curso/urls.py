
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gestion_estudiante_app/', include('gestion_estudiante_app.urls'))
]
