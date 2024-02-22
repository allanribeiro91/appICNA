from django import forms
from apps.atendimento_tecnico_digital.models import Atendimento
from setup.choices import ATIVIDADE_PRODUTIVA, TOPICO_ATENDIMENTO, STATUS_ATENDIMENTO, LISTA_HORA_ATENDIMENTO

#Adicionando opção vazia
opcao_vazia = [('', '')]
ATIVIDADE_PRODUTIVA = ATIVIDADE_PRODUTIVA + opcao_vazia
TOPICO_ATENDIMENTO = TOPICO_ATENDIMENTO + opcao_vazia
LISTA_HORA_ATENDIMENTO = LISTA_HORA_ATENDIMENTO + opcao_vazia

class AtendimentoForm(forms.ModelForm):
    atividade_produtiva = forms.ChoiceField(
        choices=ATIVIDADE_PRODUTIVA,
        widget=forms.Select(attrs={
            'class': 'form-select',
            'id':'id_atividade_produtiva'
        }),
        label='Atividade Produtiva',
        initial='',
        required=True,
    )
    topico = forms.ChoiceField(
        choices=TOPICO_ATENDIMENTO,
        widget=forms.Select(attrs={
            'class': 'form-select',
            'id':'id_topico'
        }),
        label='Tópico do atendimento',
        initial='',
        required=True,
    )
    data = forms.DateField(
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date',
        }),
        required=True,
        label='Data'
    )
    hora = forms.ChoiceField(
        choices=TOPICO_ATENDIMENTO,
        widget=forms.Select(attrs={
            'class': 'form-select',
            'id':'id_topico'
        }),
        label='Tópico do atendimento',
        initial='',
        required=True,
    )
    mais_informacoes = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control auto-expand',
            'rows': 1,
            'style': 'padding-top: 30px; height: 20vh;',
            'id': 'id_mais_informacoes'
            }),
        required=False,
        label='Mais informações'
    )
    status = forms.ChoiceField(
        choices=STATUS_ATENDIMENTO,
        widget=forms.Select(attrs={
            'class': 'form-select',
            'id':'id_status'
        }),
        label='Status do atendimento',
        initial='',
        required=True,
    )
    
    class Meta:
        model = Atendimento
        exclude = ['log_n_edicoes', 'del_status', 'del_data', 'del_usuario']

    def clean_mais_informacoes(self):
        mais_informacoes = self.cleaned_data.get('mais_informacoes')
        return mais_informacoes or "Nada informado."

