from django.shortcuts import render
from django.http import HttpResponse
from .models import Page

# Create your views here.

def welcome(request):
    return render(request, 'pages/welcome.html')

def pages(request):
    latest_pages = Page.objects.all()
    context = {'latest_pages': latest_pages}
    return render(request, 'pages/pages.html', context)
