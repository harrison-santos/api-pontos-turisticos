from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.authentication import TokenAuthentication
from avaliacoes.models import Avaliacao
from .serializer import AvaliacoesSerializer


class AvaliacoesViewSet(ModelViewSet):

    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacoesSerializer
    permission_classes = (DjangoModelPermissions, )
    authentication_classes = (TokenAuthentication, )

