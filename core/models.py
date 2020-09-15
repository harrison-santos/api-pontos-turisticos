from django.db import models
from atracoes.models import Atracao
#from comentarios.models import Comentario
from avaliacoes.models import Avaliacao
from endereco.models import Endereco

# Create your models here.
class PontosTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    atracoes = models.ManyToManyField(Atracao)
    avaliacoes = models.ManyToManyField(Avaliacao, blank=True)
    endereco = models.ForeignKey(Endereco, null=True, blank=True, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='pontos_turisticos', null=True, blank=True)

    @property
    def descricao_completa(self):
        return f'{self.nome} - {self.descricao}'

    def __str__(self):
        return self.nome

