from rest_framework import generics, status, viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from usuarios.api.serializers import UserDisplaySerializer
from mensajeria.api.serializers import ChatSerializer, MensajeSerializer

from usuarios.models import Usuario
from mensajeria.models import Chat, Mensaje
from mensajeria.api.permissions import IsAdminOrReadOnly, EsOwnerReadOnlyUOculto, EsPerfilPropioOrReadOnly

class VerListaPerfilesViewSet(mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    GenericViewSet):
    serializer_class = UserDisplaySerializer
    permission_classes = [IsAuthenticated, EsPerfilPropioOrReadOnly]

    def get_queryset(self):
        queryset = Usuario.objects.all()
        username = self.request.query_params.get("username", None)
        if username is not None:
            queryset = queryset.filter(__usuario__username=username)
        return queryset

class VerListaMisChats():
    pass

class VerChatDetalle():
    pass

class VerPerfilUsuario():
    pass 