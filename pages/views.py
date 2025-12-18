from django.shortcuts import render
from django.http import HttpResponse

# Controller, Router

# Create your views here.
def index(requests):
  return HttpResponse("<h1>Hello World</h1>")

def about(request):
  return HttpResponse("<h1>about</h1>")