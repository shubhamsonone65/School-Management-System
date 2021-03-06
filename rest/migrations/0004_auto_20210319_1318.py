# Generated by Django 3.1.7 on 2021-03-19 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0003_auto_20210319_1039'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20)),
                ('phone', models.CharField(default='', max_length=10)),
                ('role', models.CharField(choices=[('superadmin', 'superadmin'), ('teacher', 'teacher'), ('student', 'student')], max_length=20)),
                ('email', models.CharField(default='', max_length=100)),
                ('date_created', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='student',
        ),
        migrations.DeleteModel(
            name='superadmin',
        ),
        migrations.DeleteModel(
            name='teacher',
        ),
    ]
