# -*- coding:utf-8 -*-
from django import forms
from mdeditor.fields import MDTextFormField

from app.models import Blog


class BlogForms(forms.Form):
    title = forms.CharField(max_length=30, min_length=8,  help_text="请填写标题",)
    content = MDTextFormField()


class MDEditorModelForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = '__all__'