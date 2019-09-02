from django.contrib import admin
from django.urls import path
from . import views

app_name = 'blog'  # 视图函数命名空间

urlpatterns = [
    path('', views.index,name='index'),
    path('posts/<int:pk>', views.detail,name='detail'),
    path('archives/<int:year>/<int:month>', views.archives,name='archives'),
    path('category/<int:pk>', views.category,name='category'),
    # path('category/<str:category_name>', views.category,name='category'),
    path('base', views.base,name='base'),
]
