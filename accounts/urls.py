from django.urls import path
from accounts import views

app_name = "accounts"
urlpatterns = [
    # path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.signup, name="signup"),
    path('mypage/', views.mypage, name="mypage"),
    path('mypage/editname/', views.editname, name="editname"),
    path('mypage/email/', views.editemail, name="editemail"),
    path('mypage/password/', views.editpassword, name="editpassword"),
]