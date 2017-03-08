from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import UserForm
from kerkdiensten.models import User_details

def index(request):
    return render(request, 'home/index.html')

def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        row = User_details(user=user)
        row.save()
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'home/login.html', {'error_message':'Succesvol geregistreerd, je kan nu inloggen'})
    return render(request, 'home/register.html', {'form': form})

