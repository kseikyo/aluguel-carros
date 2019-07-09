from django.shortcuts import render, redirect
from .models import Carro
# Create your views here.

def carro_list_view(request):
    #Getting all cars that are not rented
	if request.user.is_authenticated:
		qs = Carro.objects.filter(alugado_por__isnull=True)
	else:
		return redirect('landing_view')
	template_name = 'carro/list.html'
	context = {'object_list': qs}
	return render(request, template_name, context)