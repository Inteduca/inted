
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('principal.urls')),
    path('inicio/', include('principal.urls')),
    path('admin/', admin.site.urls),
    path('usuario/', include('usuario.urls')),
    path('identificacion/', include('identificacion.urls'))
]
