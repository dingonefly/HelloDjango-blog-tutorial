import re

import markdown
from django.shortcuts import render, get_object_or_404
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension

from .models import Post,Category,Tag
from comments.forms import CommentForm


# Create your views here.
def index(request):
    # title= '首页'
    # welcome = 'my index'
    post_list = Post.objects.all().order_by('-created_time')
    # print(locals())
    return render(request, 'blog/index.html', locals())


def detail(request, pk):
    # 详情页
    post = get_object_or_404(Post, pk=pk)
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        # 'markdown.extensions.toc',
        TocExtension(slugify=slugify),  # 这里我无法显示为中文，原因未知
    ])

    post.body = md.convert(post.body)

    m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)
    post.toc = m.group(1) if m is not None else ''
    # print(post.toc)

    # 获取表单
    form = CommentForm()
    # print(form)
    # 获取这篇 post 下的全部评论
    comment_list = post.comments_set.all()

    # 返回到detail页面，必须提供post、comment——list、form 三个参数
    return render(request, 'blog/detail.html',locals() )


def archives(request,year,month):
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month,).order_by('-created_time')
    return render(request, 'blog/index.html', locals())

def category(request,pk):
    category_name = get_object_or_404(Category,pk=pk)

    post_list = Post.objects.filter(category=category_name).order_by('-created_time')

    return render(request, 'blog/index.html', locals())


def base(request):
    # base视图
    return render(request, 'base.html', locals())
