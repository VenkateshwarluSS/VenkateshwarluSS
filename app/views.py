from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def first(request):
    return HttpResponse('I dont know who r u')


def second(request):
    return HttpResponse('<marquee bgcolor=skyblue><h1>Thalapathy is a warrior</h1></marquee>')


def third(request):
    return HttpResponse('<h1>Bannu is very humble person</h1>')
