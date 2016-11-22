from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render(request, 'kerkdiensten/kerkdiensten.html')

@login_required
def profile(request):
    return render(request, 'kerkdiensten/profile.html')