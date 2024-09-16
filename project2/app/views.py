from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def richa(request):
    return HttpResponse('<h1><marquee>My name is Richa</marquee></h1')
