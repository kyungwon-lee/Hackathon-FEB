from django.urls import path
from blogPosts import views
from django.conf.urls import include





app_name = 'blogPosts'
urlpatterns = [
    #path('', HomePageView.as_view(), name='main'), # 'localhost:8000/posts/'
    #path('', views.main, name='main'), # 'local host:8000/mainPage/
    path('<int:id>/', views.main, name = 'main'),
    path('<int:id>/new/', views.new, name= 'new'),
    path('<int:id>/post/<int:rid>/', views.show, name= 'show'), 
    #path('<int:id>/delete', views.delete, name= 'delete'), 
    #path('<int:id>/update', views.update, name= 'update'), 
    #path('post/', include('accounts.urls')),
    path('', views.main, name='main'), # 'localhost:8000/posts/'
    path('new/', views.new, name= 'new'),
    path('<int:id>/', views.show, name= 'show'), 
    path('<int:id>/delete', views.delete, name= 'delete'), 
    #path('<int:id>/update', views.update, name= 'update'), 
    path('accounts/', include('accounts.urls')),
    path('<int:id>/comments/', views.CommentView.create, name='comment_create'),
    path('<int:id>/comments/<int:cid>/', views.CommentView.delete, name='comment_delete'),
    path('<int:id>/like/', views.LikeView.create_like, name='like'),
    path('<int:id>/dislike/', views.LikeView.create_dislike, name='dislike'),
    #path('text1/<int:id>', views.text1, name = "text1"),
    #path('text2/<int:id>', views.update, name = "update"),
    #path('text3/<int:id>', views.text3, name = "text3"),
    path('posts/text1/<int:id>', views.text1, name = "text1"),
    path('posts/text2/<int:id>', views.update, name = "update"),
    path('posts/text3/<int:id>', views.text3, name = "text3"),
]

