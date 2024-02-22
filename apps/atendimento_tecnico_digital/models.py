from django.db import models
from django.utils import timezone
from setup.choices import ATIVIDADE_PRODUTIVA, TOPICO_ATENDIMENTO, STATUS_ATENDIMENTO, LISTA_HORA_ATENDIMENTO

class Atendimento(models.Model): 

    #log
    data_registro = models.DateTimeField(auto_now_add=True)
    data_ultima_atualizacao = models.DateTimeField(auto_now=True)
    
    #dados do agendamento
    atividade_produtiva = models.CharField(max_length=120, choices=ATIVIDADE_PRODUTIVA, null=False, blank=False)
    topico = models.TextField(null=False, blank=False)
    data = models.DateField(null=False, blank=False)
    hora = models.CharField(max_length=5, choices=LISTA_HORA_ATENDIMENTO, null=False, blank=False)
    mais_informacoes = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=15, choices=STATUS_ATENDIMENTO, null=False, blank=False)

    #delete (del)
    del_status = models.BooleanField(default=False)
    del_data = models.DateTimeField(null=True, blank=True)
    del_cpf = models.CharField(max_length=14, null=True, blank=True)

    def __str__(self):
        return f"{self.id} - Data/Hora: {self.data} - {self.hora} - {self.atividade_produtiva} - Tópico(s): {self.topico}"

    def soft_delete(self, user):
        """
        Realiza uma "deleção lógica" do registro.
        """
        self.del_status = True
        self.del_data = timezone.now()
        self.del_usuario = user
        self.save()