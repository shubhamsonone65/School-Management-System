# Generated by Django 3.1.7 on 2021-03-19 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0004_auto_20210319_1318'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='role',
        ),
    ]
