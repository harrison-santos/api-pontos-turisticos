from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from atracoes.models import Atracao
from .serializers import AtracoesSerializer


class AtracoesViewSet(ModelViewSet):

    queryset = Atracao.objects.all()
    serializer_class = AtracoesSerializer
    filter_backends = (SearchFilter, )
    filter_fields = ('nome', 'descricao')
    search_fields = ('id', 'nome', 'descricao')
    lookup_field = 'nome'
