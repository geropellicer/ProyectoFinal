from rest_framework import serializers
from usuarios.models import Usuario


class UserDisplaySerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuario
        fields = ["username"]