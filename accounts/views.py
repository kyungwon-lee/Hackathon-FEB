from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import redirect

def signup(request):
    if request.method  == 'POST':
        user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
        auth.login(request, user)
        return redirect('')
    return render(request, 'accounts/signup.html')

def login(request):
    return render(request, 'accounts/login.html')