
from django.urls import path

from . import views #means from same directory import views.py

urlpatterns  = [
    path('', views.homePageView, name = 'home'), #home sometimes called index
    
]