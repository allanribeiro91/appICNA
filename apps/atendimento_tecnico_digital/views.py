from django.shortcuts import render
from apps.atendimento_tecnico_digital.forms import AtendimentoForm

def mobile(request):
    return render(request, 'atend_tecnico_digital/mobile/abas/aba_home.html')


def mob_novo_atendimento(request):

    form = AtendimentoForm()
    conteudo = {
        'form': form,
    }

    return render(request, 'atend_tecnico_digital/mobile/atendimento_tecnico/novo_atendimento.html', conteudo)
