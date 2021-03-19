# Generated by Django 3.1.7 on 2021-03-19 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=20)),
                ('phone', models.IntegerField(default='', max_length=10)),
                ('role', models.CharField(choices=[('superadmin', 'superadmin'), ('teacher', 'teacher'), ('student', 'student')], max_length=20)),
                ('email', models.CharField(default='', max_length=100)),
                ('date_created', models.DateField(auto_now_add=True)),
            ],
        ),
    ]