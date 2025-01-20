"""
URL configuration for urbandjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from task3 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('shop/', views.shop, name='shop'),
    path('cart/', views.cart, name='cart'),
]

#task4
#from django.urls import path
#from task4 import views

#urlpatterns = [
#    path('', views.index, name='index'),
#    path('shop/', views.shop, name='shop'),
#    path('cart/', views.cart, name='cart'),
#    path('games/', views.games_view, name='games'),
#]

#task5
#from django.contrib import admin
#from django.urls import path
#from task5 import views

#urlpatterns = [
#    path('admin/', admin.site.urls),
 #   path('', views.sign_up_by_html, name='sign_up_by_html'),
#    path('django_sign_up/', views.sign_up_by_django, name='sign_up_by_django'),
#]
