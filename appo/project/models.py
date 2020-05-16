from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200,db_index=True)
    image = models.ImageField(upload_to='project',blank=True)
    description = models.TextField(blank=True)
    duration = models.CharField(max_length=200,db_index=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['name']
    def __str__(self):
        return self.name