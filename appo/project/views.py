from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,get_object_or_404
from .models import Project
#首页函数
def index(request):
    project = None
    projects = Project.objects.all()
    projects_order = projects.order_by('-created')[:3]
    return render(request,'project/index.html',{'projects':projects,'projects_order':projects_order})

#项目详情函数
def project_detail(request,project_pk):
    context = {}
    projects = Project.objects.all()
    project = get_object_or_404(Project,pk=project_pk)
    context['projects'] = projects
    context['project'] = project

    return render(request,'project/project_detail.html', context)

