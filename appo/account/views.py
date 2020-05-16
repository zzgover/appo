from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'login.html', {})

#顾客登录后界面
def customer(request):
    return render(request,'project/index.html',{})

#技师登录后界面
def technician(request):
    return render(request,'book/book_detail.html',{})


def user(request):
    try:
            Userid = request.POST['userid']
            Password = request.POST['password']
            request.session["name"] =Userid
            # context={}
            # context['userid']=userid
            # request.session['msg']=context

            print(Userid)
            print(Password)
            # return render(request, 'index.html', {})
            user = User2.objects.filter(userid=Userid, password=Password)
            print(user)
            if user:
                for users in user:
                    if users.status == 'C':
                        return render(request, 'project/index.html', {})
                    if users.status == 'T':
                        return render(request, 'book/book_detail.html', {'user': user})

            else:
                return render(request, 'Work1-1.html', {'msg': '用户名或密码不正确'})
    except:
            return render(request, 'login.html', {'msg': None})


def enroll(request):
    return render(request, 'enroll.html', {})


def test(request):
    #user_name = request.POST.get("userid", None)
    #user_password = request.POST.get("password", None)
    #status = request.POST.get("status",None)
    user_name = request.POST['user_name']
    user_password = request.POST['user_password']
    status = request.POST['status']

    ## user_name=request.POST.get("userid",None)
    ## user_password=request.POST.get("password",None)

    from account.models import User2
    from account import models

    User2.objects.create(userid=user_name, password=user_password, status=status)

    info_list = models.User2.objects.all()

    return render(request, 'login.html', {"info_list": info_list})