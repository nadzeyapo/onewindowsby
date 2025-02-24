from django.shortcuts import render, get_object_or_404
from .models import Category


def home(request):
    return render(request, 'nwnd/home.html')


def procedures(request):
    return render(request, 'nwnd/procedures.html')


def juridical(request):
    return render(request, 'nwnd/juridical.html')


def architecture(request):
    return render(request, 'nwnd/architecture.html')


def education(request):
    return render(request, 'nwnd/education.html')


def housingrelations(request):
    return render(request, 'nwnd/housingrelations.html')


def laborandsocialprotection(request):
    return render(request, 'nwnd/laborandsocialprotection.html')


def money(request):
    return render(request, 'nwnd/money.html')


def stroitelstvo(request):
    return render(request, 'nwnd/stroitelstvo.html')


def svyz(request):
    return render(request, 'nwnd/svyz.html')


def oos(request):
    return render(request, 'nwnd/oos.html')


def shop(request):
    return render(request, 'nwnd/shop.html')


def sportj(request):
    return render(request, 'nwnd/sportj.html')


def finansy(request):
    return render(request, 'nwnd/finansy.html')


def imysh(request):
    return render(request, 'nwnd/imysh.html')


def doc(request):
    return render(request, 'nwnd/doc.html')


def guardianship(request):
    return render(request, 'nwnd/guardianship.html')


def sport(request):
    return render(request, 'nwnd/sport.html')


def transport(request):
    return render(request, 'nwnd/transport.html')


def nature(request):
    return render(request, 'nwnd/nature.html')


def agriculture(request):
    return render(request, 'nwnd/agriculture.html ')


def army(request):
    return render(request, 'nwnd/army.html')


def rege(request):
    return render(request, 'nwnd/rege.html')


def archieve(request):
    return render(request, 'nwnd/archieve.html')


def archieve1(request):
    return render(request, 'nwnd/archieve1.html')


def archieva2(request):
    return render(request, 'nwnd/archieva2.html')


def educationj(request):
    return render(request, 'nwnd/educationj.html')


def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    return render(request, category.template_name, {'category': category})