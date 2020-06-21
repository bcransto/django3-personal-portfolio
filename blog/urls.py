from django.urls import path, include
from django.conf import settings
from . import views, ajax

app_name = 'blog'

urlpatterns = [
    path('',views.all_blogs, name='all_blogs'),
    path('index/',views.indexView, name='index'),
    path('<int:blog_id>/', views.detail, name='detail'),
    path('post/ajax/blog', views.postBlog, name = "post_blog"),
    path('post/ajax/add', ajax.add_blog, name = "add_blog"),
    # path('post/ajax/more', ajax.more_blog, name = "more_blog"),
]
