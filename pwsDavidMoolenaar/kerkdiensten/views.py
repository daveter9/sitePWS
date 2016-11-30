from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import User_details, Kerken, Rollen

@login_required
def index(request):
    try:
      kerk = User_details.objects.get(user=request.user)
    except User_details.DoesNotExist:
        kerken = Kerken.objects.all()
        return render(request, 'kerkdiensten/kerkdiensten.html', {'kerk_keuze': kerken})
    return render(request, 'kerkdiensten/kerkdiensten.html', {'kerk': kerk,})

@login_required
def profile(request):
    user_rolls = get_object_or_404(User_details, user=request.user)
    x = user_rolls.rollen.split(',')[:-1]
    rollen_lijst = []
    for rol in x:
        y = get_object_or_404(Rollen, rol_id=rol)
        rollen_lijst.append(y)
    print(x, rollen_lijst)
    return render(request, 'kerkdiensten/profile.html', {'payload':rollen_lijst})

@login_required
def kerk_add(request):
    kerk_pk = request.POST['kerk_pk']
    kerk_to_get = get_object_or_404(Kerken, pk=kerk_pk)
    row = User_details(user=request.user, kerk=kerk_to_get, rollen='1,')
    row.save()
    return render(request, 'kerkdiensten/kerkdiensten.html', {'kerk': row,})