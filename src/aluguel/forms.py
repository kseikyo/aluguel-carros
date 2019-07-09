from django import forms
from aluguel.models import Aluguel
from carro.models import Carro

class AluguelForm(forms.Form):
    preco             = forms.DecimalField()