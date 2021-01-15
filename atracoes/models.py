from django.db import models
# Create your models here.


class Atracao(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    horario_funcionamento = models.TextField(null=True, blank=True)
    idade_minima = models.IntegerField(null=True, blank=True)
    foto = models.ImageField(upload_to='atracoes', null=True, blank=True)

    def __str__(self):
        return self.nome
