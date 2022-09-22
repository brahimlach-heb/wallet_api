from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import datetime
from django.shortcuts import render, get_object_or_404
import requests
import json
from .models import Api


# Create your views here. لازم احول لارقام

def index(request):
    apis = Api.objects.all()
    lastindex = Api.objects.all().order_by('-id')[0:1]
    if request.method == 'POST':

        ruya = int(request.POST['ruyaA'],)
        karma = int(request.POST['karmaA'],)
        adil = int(request.POST['adilA'],)
        taim = int(request.POST['taimA'],)
        efix = int(request.POST['efixA'],)
        ashab = int(request.POST['ashabA'],)
        turkpin = int(request.POST['turkpinA'],)
        razer = int(request.POST['razerA'],)
        alfurat = int(request.POST['alfuratA'],)
        musaab = int(request.POST['musaabA'],)
        abutalal = int(request.POST['abutalalA'],)
        kuvyet = int(request.POST['kuvyetA'],)
        ziraat = int(request.POST['ziraatA'],)
        codes = int(request.POST['codesA'],)
        bayilar = int(request.POST['bayilarA'],)
        depts = int(request.POST['deptsA'],)
        notes = str(request.POST['notesA'],)
        total = int(
            int(ruya) + int(karma) + int(adil) + +int(taim) + +int(efix)
            + int(ashab) + int(turkpin) + int(razer) +
            int(alfurat) + int(musaab)
            + int(abutalal) + int(kuvyet) + int(ziraat) + int(codes) + int(bayilar) + int(depts),)

        apis = Api.objects.create(

            ruya=ruya,
            karma=karma,
            adil=adil,
            taim=taim,
            efix=efix,
            ashab=ashab,
            turkpin=turkpin,
            razer=razer,
            alfurat=alfurat,
            abutalal=abutalal,
            musaab=musaab,
            kuvyet=kuvyet,
            ziraat=ziraat,
            codes=codes,
            bayilar=bayilar,
            depts=depts,
            notes=notes,
            total=total,
        )
    context = {"apis": apis, "lastindex": lastindex}
    return render(request, 'parts/index.html', context)

# .................................................


def profits(request):
    apis = Api.objects.all().order_by('-id')

    context = {"apis": apis}
    return render(request, 'parts/profits.html', context)

# .................................................


def showtotal(request):
    apis = Api.objects.all().order_by('-id')

    context = {"apis": apis}
    return render(request, 'base.html', context)

# .................................................


def store(request):

    resposne = requests.get('http://bayi.alayatl.com/servis/bakiye_kontrol.php?kod=5554443322&sifre=znet9992')
    result = resposne.text[3:]
    balance=result[:result.index("|")]
    dbt=result.removeprefix(balance+"|")
    return render(request, 'parts/store.html',{'debt':dbt,'bal':balance})
