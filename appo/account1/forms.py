import re
from django	import forms
from django.forms import widgets
from django.core.exceptions	import ValidationError

# 自定义验证规则
def mobile_validate(value):
    mobile_re = re.compile(r'^(13[0-9]|15[012356789]|17[678]|18[0-9]|14[57])[0-9]{8}$')
    if not mobile_re.match(value):
        raise ValidationError('手机号码格式错误')

class UserProfileForm(forms.Form):
    real_name = forms.CharField(
        label="真实姓名",
        required=True,
        error_messages={
            "required": "该字段不能为空",
        },
        widget=widgets.TextInput(attrs={'class': "form-control",
                                        'placeholder': '真实姓名'})
    )

    # 使用自定义验证规则
    phone = forms.CharField(
        label="电话号码",
        required=True,
        validators=[mobile_validate,],
        widget=widgets.TextInput(attrs={'class': 'form-control', 'placeholder': '电话号码'}),

        error_messages={
            "required": "该字段不能为空",
        }
    )
    address = forms.CharField(
        label="地址",
        required=True,
        widget=widgets.TextInput(attrs={'class': "form-control",
                                        'placeholder': '地址'}),
        error_messages={
            "required": "该字段不能为空",
        } )
    # group = forms.ChoiceField(
    #     label="身份",
    #     required=True,
    #     #widgets=widgets.CheckboxInput(attrs={'class': 'form-control', 'placeholder': '身份'}),
    #     error_messages = {
    #         "required": "该字段不能为空",
    #     }
    # )
