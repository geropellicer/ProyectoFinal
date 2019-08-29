from django.urls import path, include
from rest_framework.routers import DefaultRouter
from mensajeria.api.views import VerListaPerfilesViewSet

router = DefaultRouter()
router.register(r"perfiles", VerListaPerfilesViewSet, basename="perfiles")
#router.register(r"estados", EstadoPerfilViewSet, basename="estados")

urlpatterns = [
    path('', include(router.urls)),
#    path('avatar/', AvatarUpdateView.as_view(), name="avatar-update")
]



