from django.contrib.auth import authenticate, login
from django.shortcuts import render
from .forms import UserForm

def index(request):
    return render(request, 'home/index.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'home/logged_in.html')
            else:
                return render(request, 'home/login.html')
        else:
            return render(request, 'home/login.html')
    return render(request, 'home/login.html')

def user_register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'home/index.html')
    return render(request, 'home/register.html', {'form':form})