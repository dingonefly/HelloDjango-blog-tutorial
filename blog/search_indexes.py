#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/5 10:05
# @Author  : dingyifei
from haystack import indexes
from .models import Post


class PostIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Post

    def index_queryset(self, using=None):
        return self.get_model().objects.all()