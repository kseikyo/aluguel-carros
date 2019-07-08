from django.urls import path, include
from .views import carro_list_view

urlpatterns = [
    path('', carro_list_view),
]