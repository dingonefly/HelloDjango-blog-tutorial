from django.db import models
from django.utils.six import python_2_unicode_compatible
from blog.models import Post


# python_2_unicode_compatible 装饰器用于兼容 Python2
@python_2_unicode_compatible
class Comments(models.Model):
    '''评论'''
    name = models.CharField('名字',max_length=64)
    email = models.EmailField('邮箱',max_length=255)
    url = models.URLField('个人网站',blank=True)
    text = models.TextField('内容')
    created_time = models.DateTimeField('创建时间',auto_now_add=True)

    post = models.ForeignKey(Post,verbose_name='文章',on_delete=models.CASCADE)