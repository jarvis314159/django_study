# Generated by Django 2.2.1 on 2019-05-18 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20190518_1637'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Book_info',
            new_name='Book',
        ),
        migrations.AlterModelTable(
            name='book',
            table='book',
        ),
    ]
