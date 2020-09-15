from rest_framework import serializers

from atracoes.models import Atracao
from core.models import PontosTuristico
from atracoes.api.serializers import AtracoesSerializer
from endereco.api.serializer import EnderecoSerializer
from avaliacoes.api.serializer import AvaliacoesSerializer

class PontosTuristicosSerializer(serializers.ModelSerializer):
    atracoes = AtracoesSerializer(many=True)
    avaliacoes = AvaliacoesSerializer(many=True, read_only=True)
    endereco = EnderecoSerializer(read_only=True)
    #descricao_completa = serializers.SerializerMethodField()


    def criar_atracoes(self, atracoes, ponto):
        for atracao in atracoes:
            at = Atracao.objects.create(**atracao)
            ponto.atraccoes.add(at)#method add disponível em relacionamentos m to m

    def atualizar_atracoes(self):
        pass

    def create(self, validated_data):
        atracoes = validated_data['atracoes']
        del validated_data['atracoes']
        ponto = PontosTuristico.objects.create(**validated_data)#O python irá iterar chave/valor
        self.criar_atracoes(atracoes, ponto)

        return ponto

    def update(self, ):
        pass


    class Meta:
        model = PontosTuristico
        fields = ['id', 'nome', 'descricao', 'aprovado', 'foto', 'atracoes',
                  'avaliacoes', 'endereco', 'descricao_completa'
                  ]



