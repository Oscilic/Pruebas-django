from django.contrib import admin
from django.urls import path

from newcomers import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #Rutas para los recién llegados
    path('nosotros/', views.about_page, name='nosotros'),
    path('', views.home_page, name='inicio'),
    path('catalogo/', views.catalog_page, name='catalogo'),
]
