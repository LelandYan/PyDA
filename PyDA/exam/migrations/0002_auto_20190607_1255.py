# Generated by Django 2.1.7 on 2019-06-07 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_type',
            field=models.CharField(choices=[('填空', '填空'), ('选择', '选择'), ('判断', '判断')], default='选择', max_length=32),
        ),
    ]