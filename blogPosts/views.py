from django.shortcuts import render


def index(request):
    return render(request, 'blogPosts/home.html')

def main(request):
    return render(request, 'blogPosts/main.html')  

