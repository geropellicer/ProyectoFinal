from rest_framework import serializers
from usuarios.models import Amistad, Solicitud
from mensajeria.models import Chat, Mensaje
from usuarios.api.serializers import UserDisplaySerializer

class ChatSerializer(serializers.ModelSerializer):
    participante1 = UserDisplaySerializer()
    participante2 = UserDisplaySerializer()

    class Meta:
        model = Chat
        fields = '__all__'

class MensajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mensaje
        fields = "__all__"