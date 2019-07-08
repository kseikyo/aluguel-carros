from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from .models import CustomCliente

# Create your views here.
@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

    return render(request, 'login.html', {})