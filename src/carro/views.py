from django.shortcuts import render
from .models import Carro
# Create your views here.

def carro_list_view(request):
    #Getting all cars that are not rented
	qs = Carro.objects.filter(alugado_por__isnull=False)
	template_name = 'carro/list.html'
	context = {'object_list': qs}
	return render(request, template_name, context)