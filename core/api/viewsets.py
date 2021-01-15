from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer
from django.shortcuts import get_object_or_404


class PontoTuristicoViewSet(ModelViewSet):

    #queryset = PontoTuristico.objects.filter()
    serializer_class = PontoTuristicoSerializer
    filter_fields = ("nome", )
    permission_classes = (IsAuthenticatedOrReadOnly, )
    authentication_classes = (TokenAuthentication, )

    def get_queryset(self):
        queryset = PontoTuristico.objects.all()
        nome = self.request.query_params.get("nome")

        if nome:
            queryset = queryset.filter(nome=nome)
        return queryset

    # GET
    """def list(self, request, *args, **kwargs):
        return Response({"teste": "123"})

    # POST
    def create(self, request, *args, **kwargs):
        return Response({"Hello": request.POST.get("nome")})

    def destroy(self, request, *args, **kwargs):
        pass

    def retrieve(self, request, *args, **kwargs):
        return Response({"Retrive": "teste"})

    def update(self, request, *args, **kwargs):
        return Response({"Update": "teste"})

    # ACTIONS PERSONALIZADAS

    @action(methods=["get"], detail=True)
    def denunciar(self, request, pk=None):
        pass """
