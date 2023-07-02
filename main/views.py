from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from main.forms import BronForms, MenyuForms
from main.models import Bron, Categoriya, Menyu, Specials, Chefs, Galery


def create_product(request):
    model = Menyu()
    form = Menyu(request.POST, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return redirect(request,'modal.html')

def index(request):
    model = Menyu()
    form = MenyuForms(request.POST, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            messages.success(request, f'{form.instance.categoriya} Categoriya ga {form.instance.name} producti qushildi!')
            return redirect('index')
    categoriya = Categoriya.objects.all()
    course = Categoriya.objects.all()
    menu = Menyu.objects.all()
    sp = Specials.objects.all()
    chef = Chefs.objects.all()
    galery = Galery.objects.all()
    # tadbir = Tadbir.objects.all()
    if request.method == "POST":
        ism = request.POST.get('ism')
        email = request.POST.get('email')
        tel = request.POST.get('tel')
        vaqt = request.POST.get('vaqt')
        odam = request.POST.get('odam')
        xabar = request.POST.get('xabar')
        bron = Bron(
            ism=ism,
            email=email,
            tel=tel,
            vaqt=vaqt,
            odam=odam,
            xabar=xabar,
        )
        bron.save()
        messages.success(request, 'Reservation request sent please wait...')
        return redirect('index')
    model = Menyu()
    form = MenyuForms(request.POST, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            messages.success(request,
                             f'{form.instance.categoriya} Categoriya ga {form.instance.name} producti qushildi!')
            return redirect('index')
    ctx = {
        'categoriya': categoriya,
        'galery': galery,
        'menu': menu,
        'sp': sp,
        'chef': chef,
        'course':course,
        "form": form
    }
    return render(request, 'index.html', ctx)


@login_required(login_url='/acc/login')
def log(request):
    categoriya = Categoriya.objects.all()
    menu = Menyu.objects.all()
    sp = Specials.objects.all()
    # tadbir = Tadbir.objects.all()
    if request.method == "POST":
        ism = request.POST.get('ism')
        email = request.POST.get('email')
        tel = request.POST.get('tel')
        vaqt = request.POST.get('vaqt')
        odam = request.POST.get('odam')
        xabar = request.POST.get('xabar')
        bron = Bron(
            ism=ism,
            email=email,
            tel=tel,
            vaqt=vaqt,
            odam=odam,
            xabar=xabar,
        )
        bron.save()
        messages.success(request, 'Reservation request sent please wait...')
        return redirect('index')
    ctx = {
        'categoriya': categoriya,
        'menu': menu,
        'sp': sp,
        # 'tabdir': tadbir,
    }
    return render(request, 'index.html', ctx)
