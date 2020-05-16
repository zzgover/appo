from django.contrib import admin

# Register your models here.
from django import forms
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin.widgets import FilteredSelectMultiple

from django.contrib.auth.models import User, Group

class GroupAdminForm(forms.ModelForm):
    users = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        required=False,
        widget=FilteredSelectMultiple(
            verbose_name=_('Users'),
            is_stacked=False
        )
    )

    class Meta:
        model = Group
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(GroupAdminForm, self).__init__(*args, **kwargs)

        if self.instance and self.instance.pk:
            self.fields['users'].initial = self.instance.users.all()

    def save(self, commit=True):
        group = super(GroupAdminForm, self).save(commit=False)

        if commit:
            group.save()

        if group.pk:
            group.users = self.cleaned_data['users']
            self.save_m2m()

        return group

class GroupAdmin(admin.ModelAdmin):
    form = GroupAdminForm

admin.site.unregister(Group)
admin.site.register(Group, GroupAdmin)