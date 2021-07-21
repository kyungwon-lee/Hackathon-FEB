from django.urls import path
from accounts import views

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('mypage/', views.mypage, name="mypage"),
    path('mypage/editname/', views.editname, name="editname"),
    path('mypage/editemail/', views.editemail, name="editemail"),
    path('mypage/editpassword/', views.editpassword, name="editpassword"),
    path('mypage/editinterest/', views.editinterest, name = "editinterest"),
]