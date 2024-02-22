from django.urls import path
from apps.cnabr.views import consulta_usuario

urlpatterns = [
    path('consulta-usuario/<str:cpf>/<str:mensagem>/', consulta_usuario, name='consulta_usuario'),
]