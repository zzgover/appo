from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import People1,User
from book.forms import BookModelForm
#from django.core.urlresolvers import reverse
from django.shortcuts import reverse,redirect

# def book_add(request, project_id):
#     book = Book(request)
#     project = get_object_or_404(Project, id=project_id)
#     #q = int(request.POST.get('quantity'))
#     # if request.POST.get("update"):
#     #     update_q = request.POST['update']
#     # else:
#     #     update_q = False
#     book.add(p_num=num, p_name=name, P_gender=gender, p_phonenum=phonenum, p_address=address,
#                           p_project=project, pub_date=date)
#     return redirect('book:book_list')



#添加用户预约信息
def message_add(request):
    user = request.user
    model = People1
    form_class = BookModelForm
    template_name = 'book/message_add.html'
    form = BookModelForm()
    # if user is False:
    #     return redirect(reverse('account1:login'))
        #return redirect('%s?next=%s' % ('/account1/login/', request.path))  # redirect 中使用 url 格式的参数
    if request.method == 'POST':
        #print(request,FILES)
        #form = BookModelForm(request.POST,request.FILES)
        form = BookModelForm(request.POST)
        # if request.user.is_authenticated:
        #     user = request.user.username
        form.save()
        #return HttpResponse('succeed!')
    #return redirect('book:book_list')
        return redirect(reverse('book:book_list'))
    return render(request,'book/message_add.html',locals())

#保存用户预约信息
def savem(request):
    num = request.POST.get('num')
    name = request.POST.get('name')
    gender = request.POST.get('gender')
    phonenum = request.POST.get('phonenum')
    address = request.POST.get('address')
    project = request.POST.get('project')
    date = request.POST.get('date')
    People1.objects.create(user=user,p_num=num, p_name=name, P_gender=gender, p_phonenum=phonenum, p_address=address,
                          p_project=project, pub_date=date)
    # return redirect(reverse('student/yogurt_list'))
    #return redirect(reverse('book/message_list.html'))
    return render(request,'book/book_list.html')

#用户预约列表
def book_list(request):
    user = request.user
    qs_list = People1.objects.filter(user=user)
    print(qs_list)
    context = {'b_list':qs_list}
    return render(request,'book/book_list.html',context)

def book_list1(request):
    #user = request.user
    qs_list = People1.objects.all()
    print(qs_list)
    context = {'b_list':qs_list}
    return render(request,'book/book_list.html',context)


# def book_remove(request, p_id):
#     book = Book(request)
#     project = get_object_or_404(Project, id=p_id)
#     book.remove(project)
#     return redirect('book:book_list')

#删除预约信息
def delete(request):
    num = request.GET.get('orderId')
    p1=People1.objects.filter(orderId=num)
    p1.delete()
    qs_list = People1.objects.all()
    context = {'b_list': qs_list}
    return redirect(reverse('book:book_list'))
    #return JsonResponse(ret)
    #return render(request,'book/book_list.html',context)

#索引
def retrieve1(request):
	p2=People1.objects.all()
	context={'b_list':p2}
	return render(request,'book/book_list.html',context)







