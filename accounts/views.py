from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import auth
# from django.contrib.auth import get_user_model, authenticate, login
# from .models import Profile, MyAccountManager
from django.contrib.auth.models import User
# import os
from accounts.models import Profile



# def signup(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         username=request.POST.get('username')
#         password = request.POST.get('password')
#         user = get_user_model().objects.create_user(email=email, username=username, password=password)
#         try:
#             auth_user = authenticate(request, email, password)
#             print("DEBUG")
#             login(request, auth_user)
#             return redirect('/home')
#         except:
#             return redirect('/home')
#     else:
#         return render(request, 'accounts/signup.html')

def signup(request):
    if request.method == 'POST':
        user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
        user.profile.interest = request.POST['interest']
        user.profile.email = request.POST['email']
        user.save()
        auth.login(request, user)
        return redirect('/')
    else:
        return render(request, 'accounts/signup.html')


def login(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    user=User.Profile.objects.filter(email=email)
    auth.login(request, user)
    return render(request, 'blogPosts/home.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('/..')
    else:
        return render(request, '/..')

def mypage(request):
    if request.method == 'POST':
        image = request.FILES.get('photo', False)
        user = request.user
        if len(request.FILES.get('photo')) != 0:
            user.profile.profile_image = image
            user.save()
        return redirect('/accounts/mypage')
    else:
        return render(request, 'accounts/mypage.html')

def editname(request):
    if request.method == 'POST':
        user = request.user
        user.username = request.POST['username']
        user.save()
        return redirect('/accounts/mypage')
    else:
        return render(request, 'accounts/editName.html')

def editemail(request):
    if request.method == 'POST':
        user = request.user
        email = request.POST['email']
        Profile.objects.filter(user=user).update(email=email)
        return redirect('/accounts/mypage')
    else:
        return render(request, 'accounts/editEmail.html')

def editpassword(request):
    if request.method == 'POST':
        user = request.user
        old_password = request.POST['old_password']
        new_password = request.POST['new_password']

        if user.check_password(old_password):
            user.set_password(new_password)
        elif old_password != "":
            return render(request, 'accounts/mypage.html')
        return redirect('/accounts/mypage')
    else:
        return render(request, 'accounts/editPassword.html')

def editinterest(request):
    if request.method == 'POST':
        user = request.user
        interest = request.POST['interest']
        Profile.objects.filter(user=user).update(interest=interest)
        return redirect('/accounts/mypage')
    else:
        return render(request, 'accounts/editInterest.html')

