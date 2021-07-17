from django.urls import path
from blogPosts import views
from django.conf.urls import include





app_name = 'blogPosts'
urlpatterns = [
    #path('', HomePageView.as_view(), name='main'), # 'localhost:8000/posts/'
    path('', views.main, name='main'), # 'localhost:8000/posts/'
    path('new/', views.new, name= 'new'),
    path('<int:id>/', views.show, name= 'show'), 
    path('<int:id>/delete', views.delete, name= 'delete'), 
    path('<int:id>/update', views.update, name= 'update'), 
    path('accounts/', include('accounts.urls')),
    path('text1/', views.text1, name = "text1"),
    path('text2/', views.text2, name = "text2"),
    path('text3/', views.text3, name = "text3"),
]






