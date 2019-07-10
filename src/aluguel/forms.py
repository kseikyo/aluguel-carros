from django import forms
from aluguel.models import Aluguel
from carro.models import Carro

class AluguelForm(forms.Form):
    dias_de_aluguel  = forms.ChoiceField(choices=list(range(1,11)))
    preco_por_diaria = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True'}))
    total_a_pagar    = forms.DecimalField(decimal_places=2)
class AluguelModelForm(forms.ModelForm):
    class Meta:
        model  = Aluguel
        fields = ['formas_de_pagamento', 'dias_de_aluguel', 'data_inicio', 'carro', 'cliente']
        widgets = {'carro': forms.HiddenInput(), 'cliente': forms.HiddenInput()}
        labels = {
            "data_inicio": "Data de retirada:"
        }