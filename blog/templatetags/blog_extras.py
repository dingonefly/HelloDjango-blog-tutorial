#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/30 11:02
# @Author  : dingyifei
from django import template
from ..models import Post,Category,Tag
from django.db.models.aggregates import Count

register = template.Library()

@register.inclusion_tag('blog/inclusions/_recent_posts.html',takes_context=True)
def show_recent_posts(context,num=5):
    return {
        'recent_post_list':Post.objects.all().order_by('-created_time')[:num]
    }

@register.inclusion_tag('blog/inclusions/_archives.html',takes_context=True)
def show_archives(context):
    return {
        'date_list':Post.objects.dates('created_time','month',order='DESC')
    }

@register.inclusion_tag('blog/inclusions/_categories.html',takes_context=True)
def show_categories(context):
    # cate_num_dic = {}
    # category_list = Category.objects.all()
    # for cate in category_list:
    #     cate_post_num = len(cate.post_set.all())
    #     cate_num_dic[cate] = cate_post_num
    # print(cate_num_dic)
    # return cate_num_dic
    return {
        # 'category_list':Category.objects.all()
        'category_list':Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)
    }

@register.inclusion_tag('blog/inclusions/_tags.html',takes_context=True)
def show_tags(context):
    return {
        'tag_list':Tag.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)
    }