from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from cliente.forms import UserForm, CustomUserCreationForm
from django.http import Http404

def landing_view(request):
    form = CustomUserCreationForm(request.POST or None)
    if not request.user.is_authenticated:
        if form.is_valid():
            sign_up = form.save(commit=False)
            sign_up.password = make_password(form.cleaned_data['password1'])
            sign_up.status = 1
            sign_up.save()
            return redirect('/login/')
    else:
        return redirect('home_page')
    return render(request, 'land.html', {'form': form})


def login_view(request):
    form = UserForm(request.POST or None, request.FILES or None)

    if request.user.is_authenticated:
        return redirect('home_page')
    else:
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        user     = authenticate(request, username=username, password=password)
        if form.is_valid():
            if user is not None:
                if user.is_active and not user.is_staff:
                    login(request, user)
                    return redirect('home_page')
                else:
                    login(request, user)
                    return redirect('/admin')
            else:
                return redirect('login')
        
    return render(request, 'login.html', {'form': form})

def home_page(request):
    if request.user.is_authenticated:
        user = request.user
        context = {'cliente': user}
        template_name = 'home.html'
    else:
        raise Http404
        
    return render(request, template_name, context)

def logout_view(request):
    logout(request)
    return redirect('login')

    return render(request, 'login.html', {})