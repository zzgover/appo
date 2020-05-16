from django.shortcuts import render
from django.contrib.auth import	authenticate, login, logout
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, reverse,	HttpResponseRedirect
from .forms	import UserProfileForm1
from .models import	UserProfile2
from book.models import People1

from django.db.models import Q
# Create your views here.

#注册
#/account0/register/
class RegisterView(View):
    def	get(self, request):
        reg_form1 = UserCreationForm()

        # print(reg_form1)
        # print(type(reg_form1))
        for	field in reg_form1:
            field.as_widget	= field.as_widget(attrs={"class": "form-control"})

        context	= {'reg_form1': reg_form1}
        return render(request, 'account0/register.html', context)

    def	post(self, request):
        reg_form1 = UserCreationForm(request.POST)	 	 #这是django自带的创建注册表单的函数
        for	field in reg_form1:
            field.as_widget	= field.as_widget(attrs={"class": "form-control"})
        if	reg_form1.is_valid():
            reg_form1.save()
            userx =	authenticate(username=reg_form1.cleaned_data['username'],
                                   password=reg_form1.cleaned_data['password1'])
            login(request, userx)
            return redirect('book:book_list')
        else:
            return render(request, 'account0/register.html', {'reg_form1':reg_form1})
#登录
#/account0/login/
class LoginView(View):
    def	get(self, request):
        return render(request, 'account0/login.html')
    def	post(self, request):
    #接收数据
        username = request.POST.get('username')
        password = request.POST.get('password')
        context	=	{}
    #业务处理:登录校验
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
        #获取登录后所要跳转到的地址
        #默认跳转到首页
            next_url = request.GET.get('next', reverse('book:book_list1'))
            #	 跳转到 next_url
            response = redirect(next_url)
            remember = request.POST.get('keep_signed_in')
            print("*" *	20)
            print(remember)
            if remember	== '0':
                #记住用户
                response.set_cookie('username',	max_age=60 * 60 * 24 * 20)
            else:
                request.session.set_expiry(0)
            #返回 response
            return response
        else:
            context['msg'] = "用户名或密码错误"
        return	render(request, 'account0/login.html', context)
#	 注销
#	/account0/logout/
class LogoutView(View):
    '''退出登录'''
    def	get(self, request):
        '''退出登录'''
        #清除用户的 session 信息
        logout(request)
        #跳转到首页
        return redirect(reverse('project:index'))

#用户中心--个人信息
#/account0/user_center_userinfo/
class UserInfoView(View):
    def	get(self, request):
        '''用户中心--个人信息'''
        up_form = UserProfileForm1()
        user_profile = None
        try:
            user_profile = UserProfile2.objects.get(real_name=request.user)
        except UserProfile2.DoesNotExist:
            return render(request, 'account0/user_center_userinfo.html',
                          {'page': 1, 'msg': '没有用户信息', 'up_form': up_form,
                           'user_profile': user_profile})
        up_form = UserProfileForm1(
            initial={'real_name': user_profile.real_name, 'phone':
                user_profile.phone})
        return render(request, 'account0/user_center_userinfo.html',
                      {'page': 1, 'msg': ' 有用户信息 ', 'up_form': up_form,
                       'user_profile': user_profile})

    def post(self, request):
        up_form = UserProfileForm1(request.POST)

        next = request.GET.get('next', '')
        #	ret	=	{'status':	True,	'msg':	None}
        if up_form.is_valid():
            # 表单验证成功，所有经过校验的数据都保存在 up_form.cleaned_data中，这是一个字典
            have_user = UserProfile2.objects.filter(real_name=request.user).exists()
            if not have_user:
            # 创建新用户信息
                new_user = UserProfile2.objects.get_or_create(
                                          #belong_to=request.user,
                                          real_name=up_form.cleaned_data['real_name'],
                                          phone=up_form.cleaned_data['phone'])
                msg = "用户信息增加成功！"
                if next:
                    return HttpResponseRedirect(next)
            else:
                # 修改当前用户信息
                UserProfile2.objects.filter(belong_to_id__exact=request.user.pk).update(
                    real_name=up_form.cleaned_data['real_name'],
                    phone=up_form.cleaned_data['phone'])
                msg = "用户信息修改成功！"
                user_profile =UserProfile2.objects.get(belong_to_id__exact=request.user.pk)
            return render(request, 'account0/user_center_userinfo.html',
                              {'page': 1, 'msg': msg, 'up_form': up_form,
                               'user_profile': user_profile})
        else:
            return render(request, 'account0/user_center_userinfo.html',
                          {'page': 1, 'msg': '用户信息填写不正确，请输入正确信息。',	'up_form':	up_form})

