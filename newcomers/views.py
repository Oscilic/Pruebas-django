from django.shortcuts import render
from django.http import HttpResponse
from . import models as cat

def about_page(request):
    return render(request, 'newcomersTemplate/sobre_nosotros.html')
def home_page(request):
    context = {
        'services': cat.services,
        'subcat': cat.subcat,
        'products': cat.products
    }
    return render(request, 'newcomersTemplate/inicio.html', context)