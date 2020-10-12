from django.shortcuts import render
from django.http import HttpResponse


def sample(request):
    return HttpResponse("this is from service 2 and sample function")