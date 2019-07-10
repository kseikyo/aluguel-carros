from django.urls import path, include
from .views import alugar_carro

urlpatterns = [
    path('<int:id>', alugar_carro),
]