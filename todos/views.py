from django.conf.urls import url
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello World')