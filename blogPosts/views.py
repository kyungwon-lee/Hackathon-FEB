from django.shortcuts import render


def index(request):
    return render(request, 'blogPosts/home.html')

def main(request):
    return render(request, 'blogPosts/main.html')  

def home(request):
    return render(request, 'blogPosts/home.html')  

def textPage(request):
    return render(request, 'blogPosts/textPage.html')  






