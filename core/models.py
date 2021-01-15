from django.db import models
from atracoes.models import Atracao
from avaliacoes.models import Avaliacao
from endereco.models import Endereco

# Create your models here.


class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    foto = models.ImageField(
        upload_to='pontos_turisticos', null=True, blank=True)
    endereco = models.ForeignKey(
        Endereco, on_delete=models.CASCADE, null=True, blank=True)
    avaliacoes = models.ForeignKey(
        Avaliacao, on_delete=models.CASCADE, null=True, blank=True)
    atracao = models.ManyToManyField(Atracao, null=True, blank=True)

    @property
    def descricao_completa2(self):
        return "%s - %s" % (self.nome, self.descricao)

    def __str__(self):
        return self.nome
