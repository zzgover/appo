from django.db import models
from django.contrib.auth.models import User,Group

class UserProfile1(models.Model):
    belong_to =	models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    real_name =	models.CharField(max_length=100)
    #gender = models.SmallIntegerField(choices=GENDER_CHOICES)
    phone =	models.CharField(max_length=11,	default='12345678910')
    address	= models.CharField(max_length=512)
    #group = models.ForeignKey(Group,related_name='Group', on_delete=models.CASCADE)
    def	__str__(self):
        return self.real_name

    # def __str__(self):
    #     return self.gender

    def __str__(self):
        return self.phone

    def __str__(self):
        return self.address

    # def __str__(self):
    #     return self.group