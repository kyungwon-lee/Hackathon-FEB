from django.urls import path
from mainPages import views

urlpatterns = [
    path('', views.mainPage, name='mainPage'), # 'localhost:8000/mainPage/'
    path('<int:id>/', views.mainpage_section, name= 'mainpage_section'), 

]