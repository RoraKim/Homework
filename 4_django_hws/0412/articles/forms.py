from calendar import c
from tkinter import W
from django import forms                     #django builtin에서 forms 모듈 import 

class ArticleForm(forms.Form):  #forms모듈의 Form class를 상속받음
    REGION_A = 'sl'
    REGION_B = 'dj'
    REGION_C = 'gj'
    REGION_CHOICES = [
        (REGION_A, '서울'),
        (REGION_B, '대전'),
        (REGION_C, '광주'),
    ]
    
    
                 
    title = forms.CharField(max_length=10)
    content = forms.CharField(widget=forms.Textarea)           #models.py와 다르게 TextField 없음
    region = forms.ChoiceField(Widget=forms.Select, choices=REGION_CHOICES)