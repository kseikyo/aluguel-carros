from django.urls import path, include
from .views import mostrar_relatorio

urlpatterns = [
    path('<int:id>', mostrar_relatorio, name='relatorio'),
]