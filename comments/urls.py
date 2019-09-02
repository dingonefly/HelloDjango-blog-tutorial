from django.contrib import admin
from django.urls import path
from . import views

app_name = 'comments'  # 视图函数命名空间

urlpatterns = [
    path('comments/post/<int:post_pk>', views.post_comment,name='post_comment'),
]
