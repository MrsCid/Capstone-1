from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.views import View
from .forms import CustomUserCreationForm, CustomAuthenticationForm

# Create your views here.
def inicio(request):
    current_user = request.user
    userid = current_user.id
    datos = {
        'userid': userid,
        'current_user': current_user,
    }
    return render(request, 'index.html', datos)

def placa(request):
    return render(request,'patron.html')

class RegisterView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'registration/registro.html', {'form': form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('inicio')
        return render(request, 'registration/registro.html', {'form': form})

class LoginView(View):
    def get(self, request):
        form = CustomAuthenticationForm()
        return render(request, 'registration/login.html', {'form': form})

    def post(self, request):
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('inicio')
        return render(request, 'registration/login.html', {'form': form})
