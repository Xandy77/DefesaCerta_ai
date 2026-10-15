from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User


class Defesa(models.Model):
    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="defesas"
    )

    numero_auto = models.CharField(max_length=50)
    placa = models.CharField(max_length=10)
    orgao_autuador = models.CharField(max_length=150)
    estado = models.CharField(max_length=2)
    artigo_ctb = models.CharField(max_length=100)
    data_infracao = models.DateField()
    descricao_fatos = models.TextField()
    minuta = models.TextField(blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.numero_auto} - {self.placa}"
