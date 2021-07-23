from django.urls import path
from accounts import views

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('signup/leeyong', views.leeyong, name="leeyong"),
    path('signup/dogaccept', views.dogaccept, name="dogaccept"),
    path('mypage/', views.mypage, name="mypage"),
    path('mypage/editname/', views.editemail, name="editname"),
    path('mypage/editemail/', views.editname, name="editemail"),
    path('mypage/editpassword/', views.editpassword, name="editpassword"),
    path('mypage/editinterest/', views.editinterest, name = "editinterest"),
]