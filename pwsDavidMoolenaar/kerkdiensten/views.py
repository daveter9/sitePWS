from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import User_details, Kerken, Rollen, Kerkdiensten

@login_required
def index(request):
    try:
      kerk = User_details.objects.get(user=request.user)
      kerk_diensten = Kerkdiensten.objects.all().filter(kerk=kerk.kerk)
      user_details = get_object_or_404(User_details, user=request.user)
    except User_details.DoesNotExist:
        kerken = Kerken.objects.all()
        return render(request, 'kerkdiensten/kerkdiensten.html', {'kerk_keuze': kerken})

    rollen_lijst = []
    for rolz in user_details.rollen_v2.all().filter(beschikbaarheid=True):
        rollen_lijst.append(rolz)

    for dienst in kerk_diensten:
        print(dienst, dienst.beschikbaar)
        if request.user in dienst.beschikbaar.all():
            print('yay')
        else:
            print('nee')

    return render(request, 'kerkdiensten/kerkdiensten.html', {'kerk': kerk, 'kerk_diensten':kerk_diensten, 'rollen_lijst':rollen_lijst})

@login_required
def profile(request):
    user_details = get_object_or_404(User_details, user=request.user)

    return render(request, 'kerkdiensten/profile.html', {'user_details':user_details})

@login_required
def kerk_add(request):
    kerk_pk = request.POST['kerk_pk']
    kerk_to_get = get_object_or_404(Kerken, pk=kerk_pk)
    rol_to_get = get_object_or_404(Rollen, rollen='Kerklid')
    row = User_details(user=request.user, kerk=kerk_to_get, rollen='1,')
    row.save()
    t = User_details.objects.get(user=request.user)
    t.rollen_v2.add(rol_to_get)

    return render(request, 'kerkdiensten/kerkdiensten.html', {'kerk': row,})

@login_required
def dienst(request, dienst_id):
    dienst = get_object_or_404(Kerkdiensten, pk=dienst_id)

    return render(request, 'kerkdiensten/dienst.html', {'dienst':dienst})
