from django.contrib import admin
from apps.cnabr.models import Usuario, UsuarioRequisicoes


class ListandoUsuario(admin.ModelAdmin):
    list_display = ("cpf", "nome_completo", "celular", "email_pessoal", "del_status")
    list_display_links = ("cpf", "nome_completo", "celular", "email_pessoal", "del_status")
    search_fields = ("cpf", "nome_completo")
    list_per_page = 100

admin.site.register(Usuario, ListandoUsuario)
# admin.site.register(Alocacao, ListandoAlocacao)


