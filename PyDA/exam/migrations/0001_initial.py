# Generated by Django 2.1.7 on 2019-06-08 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_type', models.CharField(choices=[('F', '填空'), ('C', '选择'), ('J', '判断')], default='C', max_length=32, verbose_name='题目类型')),
                ('question_text', models.CharField(max_length=512, verbose_name='题目')),
                ('question_answer', models.CharField(max_length=128, verbose_name='题目正确答案')),
                ('question_a', models.CharField(default='无', max_length=64)),
                ('question_b', models.CharField(default='无', max_length=64)),
                ('question_c', models.CharField(default='无', max_length=64)),
                ('question_d', models.CharField(default='无', max_length=64)),
            ],
        ),
    ]
