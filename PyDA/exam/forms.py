# _*_ coding: utf-8 _*_
__author__ = 'LelandYan'
__date__ = '2019/6/7 14:13'

from django import forms

class Question(forms.Form):
    types = (
        ('F', '填空'),
        ('C', '选择'),
        ('J', '判断'),
    )
    question_type = forms.CharField(max_length=32, choices=types, default='C')
    question_text = forms.CharField(max_length=512)
    question_answer = forms.CharField(max_length=128)