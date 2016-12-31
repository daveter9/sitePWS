from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import User_details, Kerken, Rollen, Kerkdiensten, UserRoll
from collections import Counter

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

    beschikbaarheid_lijst = []
    for dienst in kerk_diensten:
        beschikbaarheid = dienst.beschikbaar.all()
        for beschikte in beschikbaarheid:
            if beschikte.user == request.user:
                beschikbaarheid_lijst.append((dienst.pk, beschikte.rol.rollen))
    #print(beschikbaarheid_lijst)

    if request.method == 'POST':
        for dienst in kerk_diensten:
            beschikbaar = dienst.beschikbaar.all().filter(user=request.user)

            pLijst = []
            for itemk in beschikbaar:
                pLijst.append(itemk.rol)

            xLijst = []
            for rolx in rollen_lijst:
                postItemsRol = request.POST.getlist(rolx.rollen)
                if len(postItemsRol) == 0:
                    pass
                else:
                    for postItemRol in postItemsRol:
                        if str(dienst.pk) == postItemRol:
                            xLijst.append(rolx)

            for onderdeel in rollen_lijst:
                if onderdeel in xLijst:
                    if onderdeel not in pLijst:
                        userRoll = get_object_or_404(UserRoll, user=request.user, rol=onderdeel)
                        dienst.beschikbaar.add(userRoll)
                else:
                    if onderdeel in pLijst:
                        userRoll = get_object_or_404(UserRoll, user=request.user, rol=onderdeel)
                        dienst.beschikbaar.remove(userRoll)

    beschikbaarheid_lijst = []
    for dienst in kerk_diensten:
        beschikbaarheid = dienst.beschikbaar.all()
        for beschikte in beschikbaarheid:
            if beschikte.user == request.user:
                    beschikbaarheid_lijst.append((dienst.pk, beschikte.rol.rollen))

    return render(request, 'kerkdiensten/kerkdiensten.html', {'kerk': kerk, 'kerk_diensten': kerk_diensten, 'rollen_lijst': rollen_lijst, 'beschikbaar': beschikbaarheid_lijst, 'user_details':user_details})

@login_required
def profile(request):
    user_details = get_object_or_404(User_details, user=request.user)

    return render(request, 'kerkdiensten/profile.html', {'user_details':user_details})

@login_required
def kerk_add(request):
    kerk_pk = request.POST['kerk_pk']
    kerk_to_get = get_object_or_404(Kerken, pk=kerk_pk)
    rol_to_get = get_object_or_404(Rollen, rollen='Kerklid')
    row = User_details(user=request.user, kerk=kerk_to_get)
    row.save()
    t = User_details.objects.get(user=request.user)
    t.rollen_v2.add(rol_to_get)

    return redirect('kerkdiensten:index')

@login_required
def dienst(request, dienst_id):
    dienst = get_object_or_404(Kerkdiensten, pk=dienst_id)

    return render(request, 'kerkdiensten/dienst.html', {'dienst':dienst})

@login_required
def rooster(request):
    user_details = User_details.objects.get(user=request.user)
    kerk_diensten = Kerkdiensten.objects.all().filter(kerk=user_details.kerk)
    rollen = Rollen.objects.all()
    rollenv2 = Rollen.objects.all().filter(beschikbaarheid=True)

    kerkDienst = kerk_diensten[1]
    kerkDienstBeschikbaarheid = kerkDienst.beschikbaar.all()

    #krijg alle beschikbaarheid van een bepaalde rol, met invoer een rolnaam
    def get_items(itemToGet, beschikbaarheid):
        x = []
        for beschikte in beschikbaarheid:
            if beschikte.rol.rollen == itemToGet:
                x.append(beschikte)
        return x

    xLijst = [1,2]
    maxRows = max(Counter(xLijst).values())

    #maak een dict van rollen met alles useroll objecten
    yDict = {}
    for rol in rollenv2:
        itemsToGet = get_items(rol.rollen, kerkDienstBeschikbaarheid)
        yDict[rol] = itemsToGet

    print(yDict)


    print(rollenv2)
    gen = False
    x = [{'name':'david'},{'name':'george'}]

    return render(request, 'kerkdiensten/rooster.html', {'user_details':user_details, 'kerk_diensten':kerk_diensten, 'rollen':rollen, 'gen':gen})