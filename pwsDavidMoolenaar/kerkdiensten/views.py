from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import User_details, Kerken, Rollen, Kerkdiensten, UserRoll, MuziekTeams, Instrumenten
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
    ingeroosterdDict = {}
    for dienst in kerk_diensten:
        ingeroosterd = dienst.ingeroosterd.all()

        ingeroosterdDict[dienst] = []
        for ingeroosterde in ingeroosterd:
            if ingeroosterde.user == request.user:
                ingeroosterdDict[dienst].append(ingeroosterde)

        beschikbaarheid = dienst.beschikbaar.all()
        for beschikte in beschikbaarheid:
            if beschikte.user == request.user:
                    beschikbaarheid_lijst.append((dienst.pk, beschikte.rol.rollen))


    return render(request, 'kerkdiensten/kerkdiensten.html', {'kerk': kerk, 'kerk_diensten': kerk_diensten, 'rollen_lijst': rollen_lijst, 'beschikbaar': beschikbaarheid_lijst, 'user_details':user_details, 'ingeroosterdDict':ingeroosterdDict})

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
def toggle_beschikbaarheid(request):
    user_details = User_details.objects.get(user=request.user)
    kerkdiensten = Kerkdiensten.objects.all().filter(kerk=user_details.kerk)
    for kerkdienst in kerkdiensten:
        kerkdienst.beschikbaarheid_open = not kerkdienst.beschikbaarheid_open
        kerkdienst.save()

    return redirect('kerkdiensten:rooster')

@login_required
def rooster(request):
    user_details = User_details.objects.get(user=request.user)
    kerk_diensten = Kerkdiensten.objects.all().filter(kerk=user_details.kerk)
    rollen = Rollen.objects.all()
    rollenv2 = Rollen.objects.all().filter(beschikbaarheid=True).exclude(rollen='Muzikant')


    kerkDienst = kerk_diensten[1]
    kerkDienstBeschikbaarheid = kerkDienst.beschikbaar.all()


    #krijg alle beschikbaarheid van een bepaalde rol, met invoer een rolnaam
    def get_items(itemToGet, beschikbaarheid):
        x = []
        for beschikte in beschikbaarheid:
            if beschikte.rol == itemToGet:
                x.append(beschikte)
        y = len(x)
        return x, y

    kerkDienstDict = {}
    ingeroosterdDict = {}
    for kerkDienst in kerk_diensten:
        kerkDienstBeschikbaarheid = kerkDienst.beschikbaar.all()

        yDict = {}
        maxRows = 0
        for rol in rollenv2:
            itemsToGet, length = get_items(rol, kerkDienstBeschikbaarheid)
            if length > maxRows:
                maxRows = length
            yDict[rol] = itemsToGet

        endList = []
        for i in range(maxRows):
            endList.append([])
            for rol in rollenv2:
                try:
                    endList[i].append(yDict[rol][i])
                except:
                    endList[i].append(None)

        kerkDienstDict[kerkDienst] = endList
        ingeroosterdDict[kerkDienst] = kerkDienst.ingeroosterd.all()



    return render(request, 'kerkdiensten/rooster.html', {'user_details':user_details, 'kerk_diensten':kerk_diensten, 'rollen':rollen, 'rollenv2':rollenv2, 'kerkDienstDict':kerkDienstDict, 'ingeroosterdDict':ingeroosterdDict,})

@login_required()
def rooster_maak(request):
    print(request.POST)
    for item in request.POST:
        try:
            int(item)
            postLijst = request.POST.getlist(item)
            print(postLijst)
            kerkdienstToGet = get_object_or_404(Kerkdiensten, pk=int(item))
            ingeroosterdToGet = kerkdienstToGet.ingeroosterd.all()
            xLijst = []
            for postItem in postLijst:
                postItem = postItem.split(':')
                userToGet = get_object_or_404(User, username=postItem[0])
                rolToGet = get_object_or_404(Rollen, rollen=postItem[1])

                userRollToGet = get_object_or_404(UserRoll, user=userToGet, rol=rolToGet)
                xLijst.append(userRollToGet)

            for ingeroosterde in ingeroosterdToGet:
                if ingeroosterde not in xLijst:
                    kerkdienstToGet.ingeroosterd.remove(ingeroosterde)

            for xItem in xLijst:
                kerkdienstToGet.ingeroosterd.add(xItem)
            print(xLijst, ingeroosterdToGet)
        except:
            pass

    return redirect('kerkdiensten:rooster')

@login_required
def rooster_muzikanten(request):
    user_details = User_details.objects.get(user=request.user)
    kerkdiensten = Kerkdiensten.objects.all().filter(kerk=user_details.kerk)
    muziekTeams = MuziekTeams.objects.all()


    superList = []
    kerkdienstDict = {}
    superList.append([])
    superList[0].append('-')
    for kerkdienst in kerkdiensten:
        kerkdienstString = '{}:{}'.format(kerkdienst.start_time, kerkdienst.soort_dienst)
        superList[0].append(kerkdienstString)
        kerkdienstDict[kerkdienst] = kerkdienst.beschikbaar.all()
    counter = len(superList)

    for muziekTeam in muziekTeams:
        superList.append([])
        superList[counter].append(muziekTeam.team)
        counter += 1
        for lid in muziekTeam.leden.all():
            superList.append([])
            lidString = '{}:{}'.format(lid.user, lid.instrument)
            superList[counter].append(lidString)

            for kerkdienst in kerkdiensten:
                if lid in kerkdienstDict[kerkdienst]:
                    superList[counter].append('beschikbaar')
                else:
                    superList[counter].append('n/a')

            counter += 1

    def krijg_instrumenten(muziekTeam):
        instrumentenLijst = set()
        ledenLijst = []
        for lid in muziekTeam.leden.all():
            ledenLijst.append(lid)
            if lid.instrument.instrument != 'Zang':
                instrumentenLijst.add(lid.instrument)
        return instrumentenLijst, ledenLijst

    def check_team_aanwezig(instrumenten, kerkdienstx, ledenLijst):
        beschikbaarheid = kerkdienstx.beschikbaar.all()
        print('beschikbaarheid: ' + str(beschikbaarheid))
        for beschikte in beschikbaarheid:
            if beschikte in ledenLijst:
                if beschikte.rol.rollen == 'Muzikant':
                    if beschikte.instrument in instrumenten:
                        instrumenten.remove(beschikte.instrument)
        if not instrumenten:
            return True
        else:
            return False

    x = muziekTeams[1]
    x1, x2 = krijg_instrumenten(x)
    print('x1: ' + str(x1))
    y = kerkdiensten[1]
    y1 = check_team_aanwezig(x1, y, x2)
    print(y1)
    #print(superList)

    return render(request, 'kerkdiensten/rooster_muzikanten.html', {'superList':superList})
