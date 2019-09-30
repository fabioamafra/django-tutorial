from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('ola mundo. voce esta no index da aplicação polls.')
