from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import auth
from .models import Profile
from django.contrib.auth.models import User

def signup(request):
    # if request.method == 'POST':
    #     user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
    #     auth.login(request, user)
    #     return redirect('/')
    # else:
    return render(request, 'accounts/signup.html')

def login(request):
    user=User.Profile.objects.filter(email=request.POST['email'])
    auth.login(request, user)
    return render(request, 'blogPosts/home.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('/..')
    else:
        return render(request, '/..')

def mypage(request):
    return render(request, 'accounts/mypage.html')

def editname(request):
    return render(request, 'accounts/editName.html')

def editemail(request):
    return render(request, 'accounts/editEmail.html')

def editpassword(request):
    return render(request, 'accounts/editPassword.html')
