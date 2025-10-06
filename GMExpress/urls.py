from django.contrib import admin
from django.urls import path

from newcomers import views

urlpatterns = [
<<<<<<< HEAD
    path('', admin.site.urls),
=======
    path('admin/', admin.site.urls),
    #Rutas para los recién llegados
    path('nosotros/', views.about_page, name='nosotros'),
    path('', views.home_page, name='inicio')
>>>>>>> 03111694c037b4df1ddfc8be2ffdf62509412168
]
