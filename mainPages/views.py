from django.shortcuts import render
from .models import MainPage_section

# Create your views here.

def mainPage(request) :
    return render(request, 'blogPosts/main.html')

def mainpage_section(request,id) :
    section = MainPage_section.objects.get(id = id)
    return render(request, 'blogPosts/main.html', {'post':section})


