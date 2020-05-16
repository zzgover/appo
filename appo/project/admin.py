from django.contrib import admin
from .models import Project
# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
	list_display = ['name','duration','price','image']
	list_filter = ['name','duration','price']
	list_editable = ['duration','price']

admin.site.register(Project,ProjectAdmin)
