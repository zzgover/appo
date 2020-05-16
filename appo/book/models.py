from django.db import models
from django import forms
# Create your models here.
#from appo.project.models import Project
from project.models import Project
from django.contrib.auth.models import User

GENDER_CHOICES=((1,'男'),
                (0,'女'))

# class BookManager(models.Manager):
#     def save_from_object(self, request, obj):
#         book = People1()
#         book.object_id = obj.id
#         book.operation_by = request.user
#         book.save()

#用户预约信息
class People1(models.Model):
    orderId = models.AutoField(max_length=128, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user',null=True,default=User.is_authenticated)
    p_name = models.CharField(max_length=200,db_index=True)
    P_gender = models.SmallIntegerField(choices=GENDER_CHOICES)
    p_phonenum = models.CharField(max_length=30, null=False)
    p_address = models.CharField(max_length=200,default='（乌鲁木齐市XX区XX街道XX小区XX栋XX号）')
    p_project = models.ForeignKey(Project, related_name='Project', on_delete=models.CASCADE)
    pub_date = models.DateTimeField('时间', null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['updated']
    def __str__(self):
        return self.p_name

    def __str__(self):
        return 'Book {}'.format(self.user)

    # objects = BookManager()

# class MyBlogForm(forms.ModelForm):
#     class Meta:
#         model = People1 # btw I'd use Capital Letters For Classes
#
#     def save(self, *args, **kwargs):
#         super(MyBlogForm, self).save(*args, **kwargs)
#         People1.objects.save_from_object(request, self.instance)