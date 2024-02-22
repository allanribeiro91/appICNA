from django.urls import path
from apps.atendimento_tecnico_digital.views import mobile, mob_novo_atendimento

urlpatterns = [
    path('mobile/', mobile, name='mobile'),
    path('mobile/novo-atendimento/', mob_novo_atendimento, name='mob_novo_atendimento'),
]