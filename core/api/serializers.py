from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from atracoes.models import Atracao
from core.models import PontoTuristico
from atracoes.api.serializers import AtracaoSerializer
from endereco.api.serializers import EnderecoSerializer
from avaliacoes.api.serializer import AvaliacoesSerializer


class PontoTuristicoSerializer(serializers.ModelSerializer):
    atracao = AtracaoSerializer(many=True)
    avaliacoes = AvaliacoesSerializer(read_only=True)

    class Meta:
        model = PontoTuristico
        fields = ("id", "nome", "descricao", "aprovado", "foto",
                  "endereco", "avaliacoes", "atracao", "avaliacoes",
                  "avaliacoes", "descricao_completa2"
                  )

    def get_descricao_completa(self, obj):
        return "%s - %s" % (obj.nome, obj.descricao)
