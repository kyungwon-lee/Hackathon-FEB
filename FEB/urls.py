"""FEB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include 
import blogPosts.views
import accounts.views

app_name= "blogPosts"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blogPosts.views.index, name='index'),
    path('main/', blogPosts.views.main, name='main'),
    path('home/', blogPosts.views.home, name='home'),
    path('textPage/', blogPosts.views.textPage, name='textPage'),
    path('example/', blogPosts.views.example, name='example'),
    path('posts/', include('blogPosts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', accounts.views.signup, name="signup"),
    path('accounts/mypage/', accounts.views.mypage, name="mypage"),
    path('accounts/mypage/editname/', accounts.views.editname, name="editname"),
    path('accounts/mypage/email/', accounts.views.editemail, name="editemail"),
    path('accounts/mypage/password/', accounts.views.editpassword, name="editpassword"),
]


