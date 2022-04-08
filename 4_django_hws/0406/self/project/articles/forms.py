from email import contentmanager
from turtle import title
from django import forms

class ArticleForm(forms.Forms):
    title = forms.CharField(max_length=10)
    content = forms.CharField(widget=forms.Textarea)

