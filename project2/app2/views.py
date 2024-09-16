from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def preeti(request):
    return HttpResponse('<h1><marquee>My name is preeti</marquee></h1')
