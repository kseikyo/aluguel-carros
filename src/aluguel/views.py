from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from carro.models import Carro
# Create your views here.

@login_required
def alugar_carro(request, id):
    obj = get_object_or_404(Carro, id=id)
    template_name= 'aluguel/alugar.html'
	context = {"object": obj}
	return render(request, template_name, context)