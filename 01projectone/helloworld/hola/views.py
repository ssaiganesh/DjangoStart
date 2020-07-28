from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def homePageView(request):#always pass request
    return HttpResponse('Hola mean Hello in Spanish')
