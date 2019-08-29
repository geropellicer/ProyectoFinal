from django.urls import path
from usuarios.api.views import CurrentUserAPIView

urlpatterns = [
    path("usuario/", CurrentUserAPIView.as_view(), name="current-user")
]