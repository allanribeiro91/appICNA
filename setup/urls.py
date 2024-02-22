from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.cnabr.urls')),
    path('', include('apps.atendimento_tecnico_digital.urls')),

    path('__reload__/', include('django_browser_reload.urls'))
]
