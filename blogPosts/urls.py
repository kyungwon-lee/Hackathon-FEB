from django.urls import path
from blogPosts import views
from django.conf.urls import include



app_name = 'blogPosts'
urlpatterns = [
    path('', views.example, name='example'), # 'localhost:8000/posts/'
    path('new/', views.new, name= 'new'),
    path('<int:id>/', views.show, name= 'show'), 
    path('<int:id>/delete', views.delete, name= 'delete'), 
    path('<int:id>/update', views.update, name= 'update'), 
    path('accounts/', include('accounts.urls')),
    path('<int:id>/comments/', views.CommentView.create, name='comment_create'),
    path('<int:id>/comments/<int:cid>/', views.CommentView.delete, name='comment_delete'),
    path('<int:id>/like/', views.LikeView.create_like, name='like'),
    path('<int:id>/dislike/', views.LikeView.create_dislike, name='dislike'),
]