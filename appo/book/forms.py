from django import forms
from .models import People1
from django.contrib.auth.models import User
class BookModelForm(forms.ModelForm):
    class Meta:
        model = People1

        fields = '__all__'  # __all__为所有字段
        #user = forms.Textarea(labels='当前账户', widget=forms.Textarea(attrs={'class': 'form-control'}))
        labels = {
            'user':'当前账户',
            'p_name': '姓名',
            'P_gender': '性别',
            'p_phonenum': '电话',
            'p_address': '地址',
            'p_project': '项目',
            'pub_date': '时间'

        }
        widgets = {
            #'user' : forms(request.user.is_authenticated,attrs={'class': 'form-control'}),
            'p_name' : forms.widgets.TextInput(attrs={'class': 'form-control'}),
            'P_gender' : forms.widgets.Select(attrs={'class': 'form-control'}),
            'p_phonenum' : forms.widgets.TextInput(attrs={'class': 'form-control'}),
            'p_address' : forms.widgets.TextInput(attrs={'class': 'form-control'}),
            #'pub_date' : forms.widgets.TimeInput(attrs={'type': 'date','class': 'form-control'}),
            'p_project' : forms.widgets.Select(attrs={'class': 'form-control'}),

        }  # 必须按定义的字段顺序排列
        #pub_date = forms.DateField(label='预约时间', widget=forms.DateInput(attrs={'type': 'date'}))
        # def save(self, *args, **kwargs):
        #     super(BookModelForm, self).save(*args, **kwargs)
        #     People1.objects.save_from_object(request, self.instance)

