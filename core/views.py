from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm



def home(request):
    """ comprueba si estamos o no identificados """

    if request.user.is_authenticated:
        return render(request, 'core/home.html')
    else:
        return redirect('/login')

def iniciar_sesion(request):
    """ pantalla de login """

    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')

    return render(request, 'core/login.html', {'form': form})

def cerrar_sesion(request):
    """ cerrar la sesión """

    logout(request)
    return redirect('/')