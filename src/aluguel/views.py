from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from carro.models import Carro
from aluguel.models import Aluguel
from cliente.models import CustomCliente
from aluguel.forms import AluguelModelForm
# Create your views here.

@login_required
def alugar_carro(request, id):
    form = AluguelModelForm(request.POST or None, initial={'carro': Carro.objects.get(id=id), 'cliente': request.user})
    if form.is_valid():
        new_form = form.cleaned_data
        carro               = new_form["carro"] 
        cliente             = new_form['cliente']
        formas_de_pagamento = new_form['formas_de_pagamento']
        dias_de_aluguel     = new_form['dias_de_aluguel']
        Aluguel.objects.create(carro=carro, cliente=cliente, formas_de_pagamento=formas_de_pagamento, dias_de_aluguel=dias_de_aluguel, total=dias_de_aluguel*carro.preco)
        carro.alugado_por = cliente
        return redirect('home_page')

    obj = get_object_or_404(Carro, id=id)
    template_name= 'aluguel/alugar.html'
    context = {"carro": obj, 'form': form}
    return render(request, template_name, context)