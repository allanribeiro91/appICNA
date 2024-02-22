from django.shortcuts import render, HttpResponse
from apps.cnabr.models import Usuario

def consulta_usuario(request, cpf=None, mensagem=None):

    if cpf == None:
        return HttpResponse('CPF não informado')

    #função para validar o CPF: quantidade de números, válido
    #verificar se o CPF tem traços e pontos
    #verificar se a mensagem foi inclusa

    print('Mensagem: ', mensagem)
    try:
        usuario = Usuario.objects.get(cpf=cpf)
        response_message = f"Usuário encontrado: {usuario}"
        return HttpResponse(response_message)
    except Usuario.DoesNotExist:
        return HttpResponse('Usuário não encontrado')

