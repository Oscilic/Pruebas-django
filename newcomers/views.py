from django.shortcuts import render
from django.http import HttpResponse

def about_page(request):
    return render(request, 'newcomersTemplate/sobre_nosotros.html')
def home_page(request):
    return render(request, 'newcomersTemplate/inicio.html')
def catalog_page(request):
    return render(request, 'newcomersTemplate/catalogo.html')