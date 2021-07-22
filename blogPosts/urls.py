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
    #path('new/', views.new, name= 'new'),
    #path('<int:id>/', views.show, name= 'show'), 
    path('<int:id>/delete', views.delete, name= 'delete'), 
    #path('<int:id>/update', views.update, name= 'update'), 
    path('accounts/', include('accounts.urls')),
    path('<int:id>/post/<int:rid>/comments/', views.CommentView.create, name='comment_create'),
    path('<int:id>/post/<int:rid>/comments/<int:cid>/', views.CommentView.delete, name='comment_delete'),
    path('<int:id>/post/<int:rid>/like/', views.LikeView.create_like, name='like'),
    path('<int:id>/post/<int:rid>/dislike/', views.LikeView.create_dislike, name='dislike'),
    path('content/<int:id>/', views.IframeView.content, name = "content"),
    path('update/<int:id>/', views.IframeView.update, name = "update"),
    path('history/<int:id>/', views.IframeView.history, name = "history"),
    path('editors/<int:id>/',  views.EditorView.create, name='editors'),
]

