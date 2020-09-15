from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from core.models import PontosTuristico
from .serializers import PontosTuristicosSerializer
from django.shortcuts import get_object_or_404


class PontosTuristicosViewSet(ModelViewSet):

    queryset = PontosTuristico.objects.all()
    serializer_class = PontosTuristicosSerializer
    permission_classes = (DjangoModelPermissions, )
    authentication_classes = (TokenAuthentication, )




    def get_queryset(self):
        #Utilizando query parameters para filtrar
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)
        queryset = PontosTuristico.objects.all()#lazy loading
        if id:
            queryset = PontosTuristico.objects.filter(pk=id)
        if nome:
            queryset = queryset.objects.filter(nome=nome)
        if descricao:
            queryset = queryset.objects.filter(descricao=descricao)

        return PontosTuristico.objects.filter()# This must be an iterable, and may be a queryset.

    #METHOD GET
    '''
    def list(self, request, *args, **kwargs):
        return Response({'teste': 'teste'})'''

    #METHOD POST


    #METHOD DELETE
    # TODO: Verificar se usuário tem permissão; fazer log de quem deletou; flag deletado == true para usuario
    def destroy(self, request, pk=None):
        ponto = get_object_or_404(self.queryset, pk=pk)
        ponto.delete()
        #serializer = PontosTuristicosSerializer(ponto)
        print(ponto)
        return Response(status=status.HTTP_204_NO_CONTENT)

    #METHOD GET COM PK
    def retrieve(self, request, pk=None):
        ponto = get_object_or_404(self.queryset, pk=pk)
        serializer = PontosTuristicosSerializer(ponto)
        return Response(serializer.data)

    #METHOD PUT
    '''def update(self, request, *args, **kwargs):
        pass'''

    #METHOD PATCH
    def partial_update(self, request, *args, **kwargs):
        pass


    #CUSTOM ACTION - dominio/v1/pontoturistico/1/denunciar/
    @action(methods=['GET', 'POST'], detail=True)#detail == true é necessário passar a pk
    def denunciar(self, request, pk):
        pass