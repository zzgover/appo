from django.db import models
from django.contrib.auth.models import User

class UserProfile2(models.Model):
    #belong = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
    real_name = models.CharField(max_length=100)
    phone =	models.CharField(max_length=11,	default='12345678910')
    def	__str__(self):
        return self.real_name
    def __str__(self):
        return self.phone
