from django.conf.urls import url
from django.urls import path, include
from .import views

app_name = 'project'
urlpatterns = [
 ## path('',views.index,name='index'),
 ## path('project_detail/<int:a>',views.project_detail,name='project_detail')

 url(r'^$',views.index,name='index'),
 url(r'^Project_detail/(?P<project_pk>[0-9]+)/$',views.project_detail,name='project_detail'),
]