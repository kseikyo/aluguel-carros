from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from .models import CustomCliente
from carro.models import Carro
from aluguel.models import Aluguel
from django.http import Http404

# Create your views here.
@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

    return render(request, 'login.html', {})

def mostrar_relatorio(request, id):
    aluguel = Aluguel.objects.get(cliente=CustomCliente.objects.get(id=id))
    if aluguel is not None :
        context = {'aluguel': aluguel}
        template_name = 'relatorio.html'
    else:
        raise Http404

    return render(request, template_name, context)