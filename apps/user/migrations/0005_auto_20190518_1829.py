# Generated by Django 2.2.1 on 2019-05-18 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20190518_1814'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='uage',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='upwd',
            field=models.CharField(default='', max_length=20),
        ),
    ]
