from django.db.models.signals import pre_save
from django.dispatch import receiver
from mensajeria.models import Mensaje, Chat
from usuarios.models import Usuario, Amistad, Solicitud

#Creamos la senial de que si se completa una amistad, se crea un chat
@receiver(pre_save, sender=Amistad)
def crear_chat_en_amistad(sender, instance, *args, **kwargs):
    persona1 = instance.amigoPropone
    persona2 = instance.amigoPropuesto
    chats1 = Chat.objects.filter(participante1=persona1, participante2=persona2)
    chats2 = Chat.objects.filter(participante1=persona2, participante2=persona1)
    if not chats1 and not chats2:
        chat = Chat(participante1=persona1, participante2=persona2)
        chat.save()

@receiver(pre_save, sender=Mensaje)
def revisar_mensajes_nuevos(sender, instance, *args, **kwargs):
    pass
    #cuando un nuevo mensaje es creado, si tiene al usuario como recipiente, actualice

#Cuando una amistad esta por ser pasada de false a true (aceptada) la borramos y creamos su correspondiente amistad
@receiver(pre_save, sender=Solicitud)
def confirmar_amistad(sender, instance, *args, **kwargs):
    #Chequeamos si el confirmado de la instancia de la SOLICITUD que nos estan pasando es true
    if instance.confirmada:
        amigo1 = instance.solicitado
        amigo2 = instance.solicitante
        amis1 = Amistad.objects.filter(amigoPropone=amigo1, amigoPropuesto=amigo2)
        amis2 = Amistad.objects.filter(amigoPropone=amigo2, amigoPropuesto=amigo1)
        if not amis1 and not amis2:
            amis = Amistad(amigoPropone=amigo1, amigoPropuesto=amigo2)
            amis.save()

