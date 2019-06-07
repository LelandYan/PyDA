from django.db import models


# Create your models here.
class User(models.Model):
    '''用户信息表'''
    gender = (
        ('male', '男'),
        ('female', '女'),
    )
    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender, default='男')
    c_time = models.DateTimeField(auto_now_add=True)
    is_work = models.IntegerField(default=0)
    not_solve = models.IntegerField(default=0)
    is_exam = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['c_time']
        verbose_name = '用户'
        verbose_name_plural = '用户'
