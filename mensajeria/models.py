from django.db import models
from usuarios.models import Usuario

# Create your models here.
class Chat(models.Model):
    participantes = models.ManyToManyField(Usuario, related_name="chats")

    def __str__(self):
        return 'Chate de ', self.participantes

class Mensaje(models.Model):
    de = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="mensajes_de")
    para = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="mensajes_para")
    fecha_creado = models.DateTimeField(auto_now_add=True)
    fecha_recibido = models.DateTimeField(blank=True, null=True)
    texto = models.TextField(blank=False)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name="mensajes")

    def __str__(self):
        return self.texto
