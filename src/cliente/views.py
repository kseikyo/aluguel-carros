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
    try:
        aluguel = Aluguel.objects.filter(cliente=CustomCliente.objects.get(id=id))
        if aluguel:
            context = {'alugueis': aluguel}
            template_name = 'relatorio.html'
        else:
            template_name = 'sem_alugueis.html'
            context = {}
        if request.method == 'POST':
            carro   = Carro.objects.get(nome=request.POST['carro_nome'])
            print(carro)
            aluguel = Aluguel.objects.get(carro=carro) 
            print(aluguel)
            aluguel.delete()
            carro.alugado_por = None
            carro.save()
            return redirect('home_page')
        
    except:
        template_name = 'sem_alugueis.html'
        context = {}
    return render(request, template_name, context)