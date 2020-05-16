from django.db import models

# Create your models here.
from django.contrib.auth.models import Group
from django.contrib.auth.models import User

class User2(models.Model):
    id = models.AutoField(primary_key=True)
    userid = models.CharField(max_length=20)
    password = models.CharField(max_length=15)
    status = models.CharField(max_length=15,null=True)
    def __str__(self):
        # 在Python3中使用 def __str__(self):
        return self.userid
    def __str__(self):
        # 在Python3中使用 def __str__(self):
        return self.password
    def __str__(self):
        # 在Python3中使用 def __str__(self):
        return self.status