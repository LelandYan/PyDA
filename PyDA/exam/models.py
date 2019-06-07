from django.db import models
from datetime import datetime

# Create your models here.
class Question(models.Model):
    types = (
        ('F', '填空'),
        ('C', '选择'),
        ('J', '判断'),
    )
    question_type = models.CharField(max_length=32, choices=types, default='C')
    question_text = models.CharField(max_length=512)
    question_answer = models.CharField(max_length=128)
    # is_right = models.IntegerField(default=0)
    # is_answer = models.IntegerField(default=0)
    # create_time = models.DateTimeField('create_time', default=datetime.now)
    # update_time =models.DateTimeField('update_time', default=datetime.now)
    question_a = models.CharField(max_length=64,default="无")
    question_b = models.CharField(max_length=64,default="无")
    question_c = models.CharField(max_length=64,default="无")
    question_d = models.CharField(max_length=64,default="无")

    def __str__(self):
        return self.question_text
# class Paper(models.Model):
#     is_activate = models.BooleanField(default=False)

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=128)

    def __str__(self):
        return self.answer
