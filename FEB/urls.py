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
from django.conf import settings 
from django.conf.urls.static import static
import blogPosts.views
from django.conf import settings
from django.conf.urls.static import static


app_name= "FEB"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blogPosts.views.home, name='home'),

    #path('main/', blogPosts.views.main, name='main'), 
    #path('main/', include('mainPages.urls')),
    #path('textPage/', blogPosts.views.textPage, name='textPage'),
    path('mainPage/', include('blogPosts.urls')),
    #path('mainPage/<int:id>/', include('blogPosts.urls')),
    #path('mainPage/', include('mainPages.urls')), 
    

    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


