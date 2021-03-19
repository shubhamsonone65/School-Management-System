from django.db import models

# Create your models here.
class User(models.Model):
    # id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=20,default="")
    phone=models.CharField(max_length=10,default="")
    email=models.CharField(max_length=100,default="")
    date_created=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


    