from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def serv1hello(request):
    return HttpResponse("this is from serv1hello")