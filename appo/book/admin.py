from django.contrib import admin
from .models import People1
from django.contrib.auth.models import User


# # Register your models here.
# class BookItemInline(admin.TabularInline):
#     model = User
#     #raw_id_fields = ['project']
#
# class BookAdmin(admin.ModelAdmin):
#     list_display = ['user', 'p_name', 'P_gender', 'p_phonenum', 'p_address', 'p_project', 'pub_date']
#     list_filter = ['user', 'p_name', 'p_project']
#     date_hierarchy = 'pub_date'
#     inlines = [BookItemInline]
#
# admin.site.register(People1, BookAdmin)

# class BookAdmin(admin.ModelAdmin):
#   exclude = ('user',)
#   list_display = ('user', 'pub_date')
#   #prepopulated_fields = { 'slug': ['name'] }
#   def has_change_permission(self, request, obj=None):
#     has_class_permission = super(BookAdmin, self).has_change_permission(request, obj)
#     if not has_class_permission:
#       return False
#     if obj is not None and not request.user.is_superuser and request.user.id != obj.user_id:
#       return False
#     return True
#
#   def queryset(self, request):
#     if request.user.is_superuser:
#       return People1.objects.all()
#     return People1.objects.filter(user=request.user)
#
#   def save_model(self, request, obj, form, change):
#     if not change:
#       obj.user = request.user
#     obj.save()
#
# admin.site.register(People1, BookAdmin)

#@xadmin.sites.register(People1)
class PeopleAdmin(object):
    list_display = ("user", "p_name", "P_gender", "p_phonenum", "p_address", "p_project", "pub_date")
    list_display_links = ("name",)

    def save_models(self):
        self.new_obj.user = self.request.user.is_authenticated
        super().save_models()
