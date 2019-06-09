from django.db import models
from datetime import datetime
from user.models import User
# Create your models here.
# class Paper(models.Model):
#     name = models.CharField(max_length=128,unique=True,verbose_name="试卷名称")
#     is_activate = models.BooleanField(default=False,verbose_name="试卷状态")
#     score = models.IntegerField(default=0,verbose_name="总分")
#     begin_time = models.DateTimeField("begin_time",default=datetime.now,verbose_name="开始时间")
#     end_time = models.DateTimeField("end_time",default=datetime.now,verbose_name="结束时间")
#
#     def __str__(self):
#         return self.name
#
class Question(models.Model):
    types = (
        ('F', '填空'),
        ('C', '选择'),
        ('J', '判断'),
    )
    #paper = models.ForeignKey(Paper,on_delete=models.CASCADE,verbose_name="试卷")
    question_type = models.CharField(max_length=32, choices=types, default='C',verbose_name="题目类型")
    question_text = models.CharField(max_length=512,verbose_name="题目")
    question_answer = models.CharField(max_length=128,verbose_name="题目正确答案")
    #is_right = models.IntegerField(default=0,verbose_name="正确次数")
    #is_answer = models.IntegerField(default=0,verbose_name="回答次数")
    #create_time = models.DateTimeField('create_time', default=datetime.now,verbose_name="创建时间")
    #update_time =models.DateTimeField('update_time', default=datetime.now,verbose_name="更新时间")
    question_a = models.CharField(max_length=64,default="无")
    question_b = models.CharField(max_length=64,default="无")
    question_c = models.CharField(max_length=64,default="无")
    question_d = models.CharField(max_length=64,default="无")
#
#     def __str__(self):
#         return self.question_text
#
# class Answer(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     answer = models.CharField(max_length=128)
#
#     def __str__(self):
#         return self.answer


###################################################
# class SelectInfo(models.Model):
#     """
#     选择题库表
#     """
#     id_n = models.CharField(max_length=128,verbose_name="题目编号",unique=True,null=False,blank=False)
#     question_text = models.CharField(max_length=512, verbose_name="题目",null=False,blank=False)
#     """
#     null=True
# 　　数据库中字段可以为空
#     blank=True
# 　　django的 Admin 中添加数据时可允许空值"""
#     qa = models.CharField(max_length=100,null=False,blank=False)
#     qb = models.CharField(max_length=100,null=False,blank=False)
#     qc = models.CharField(max_length=100,null=False,blank=False)
#     qd = models.CharField(max_length=100,null=False,blank=False)
#     answer = models.CharField(max_length=20,null=False,blank=False)
#
#     def __str__(self):
#         return self.id_n
#
# class JudgeInfo(models.Model):
#     """
#     判断题库表
#     """
#     id_n = models.CharField(max_length=128, verbose_name="题目编号", unique=True, null=False, blank=False)
#     question_text = models.CharField(max_length=512, verbose_name="题目", null=False, blank=False)
#     answer = models.CharField(max_length=20, null=False, blank=False)
#     def __str__(self):
#         return self.id_n
#
#
# class FillBlankInfo(models.Model):
#     """
#     填空题库表
#     """
#     id_n = models.CharField(max_length=128, verbose_name="题目编号", unique=True, null=False, blank=False)
#     question_text = models.CharField(max_length=512, verbose_name="题目", null=False, blank=False)
#     answer = models.CharField(max_length=32, null=False, blank=False)
#     def __str__(self):
#         return self.id_n
#
#
# class ExamInfo(models.Model):
#     """
#     试卷表
#     """
#     id_n = models.CharField(max_length=128, verbose_name="试卷编号", unique=True, null=False, blank=False)
#     len_time = models.IntegerField(null=False,blank=False,verbose_name="考试时长")
#     num_judge = models.IntegerField(null=True,blank=True,verbose_name="判断题数量")
#     val_judge = models.FloatField(null=True,blank=True,verbose_name="判断题分数")
#     num_select = models.IntegerField(null=True, blank=True, verbose_name="选择题数量")
#     val_select = models.FloatField(null=True, blank=True, verbose_name="选择题分数")
#     num_fill = models.IntegerField(null=True, blank=True, verbose_name="填空题数量")
#     val_fill = models.FloatField(null=True, blank=True, verbose_name="填空题分数")
#
# class ScoreInfo(models.Model):
#     """
#     成绩表
#     """
#     user_id = models.ForeignKey(User.name,on_delete=models.CASCADE,verbose_name="用户编号")
#     exam_id = models.ForeignKey(ExamInfo.id_n,on_delete=models.CASCADE,verbose_name="考试编号")
#     score = models.FloatField(max_length=10,null=False,blank=False,verbose_name="成绩")
#     state = models.IntegerField(verbose_name="考试状态")
#     exam_time = models.DateTimeField(null=False,blank=False,verbose_name="考试时间")
