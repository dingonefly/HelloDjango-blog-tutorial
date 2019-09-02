#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/2 15:42
# @Author  : dingyifei
from django import forms
from .models import Comments

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['name','email','url','text']