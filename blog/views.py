from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post
import markdown

# Create your views here.
def index(request):
    # title= '首页'
    # welcome = 'my index'
    post_list = Post.objects.all().order_by('-created_time')
    # print(locals())
    return render(request,'blog/index.html',locals())

def detail(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.body = markdown.markdown(post.body,
                                  extension=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    return render(request,'blog/detail.html', context={'post': post})

def base(request):
    return render(request,'base.html',locals())