from django.contrib import admin
from django.urls import path,include
from . import views
from blog.feeds import AllPostsRssFeed

app_name = 'blog'  # 视图函数命名空间

urlpatterns = [
    # path('', views.index,name='index'),
    path('', views.IndexView.as_view(),name='index'),
    # path('posts/<int:pk>', views.detail,name='detail'),
    path('posts/<int:pk>', views.PostDetailView.as_view(),name='detail'),
    path('archives/<int:year>/<int:month>', views.archives,name='archives'),
    # path('category/<int:pk>', views.category,name='category'),
    path('category/<int:pk>', views.CategoryView.as_view(),name='category'),
    # path('category/<str:category_name>', views.category,name='category'),
    path('tag/<int:pk>', views.TagView.as_view(), name='tag'),
    path('base', views.base,name='base'),
    path('all/rss', AllPostsRssFeed(), name='rss'),
    # path('search', views.search, name='search'),
    path('search', include('haystack.urls')),
]
