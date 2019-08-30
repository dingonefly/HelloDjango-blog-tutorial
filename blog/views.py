import re

import markdown
from django.shortcuts import render, get_object_or_404
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension

from .models import Post


# Create your views here.
def index(request):
    # title= '首页'
    # welcome = 'my index'
    post_list = Post.objects.all().order_by('-created_time')
    # print(locals())
    return render(request, 'blog/index.html', locals())


def detail(request, pk):
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

    return render(request, 'blog/detail.html', context={'post': post})


def base(request):
    return render(request, 'base.html', locals())
