from rest_framework import serializers
from avaliacoes.models import Avaliacao


class AvaliacoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = ['id', 'usuario', 'comentario', 'nota']