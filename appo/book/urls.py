from django.conf.urls import url
from django.urls import path, include
from .import views
from django.contrib.auth.decorators import login_required
app_name = 'book'
urlpatterns = [
    path('message_add/',login_required(views.message_add),name='message_add'),
    path('savem/',views.savem,name='savem'),
#    path('message_detil',views.message_detil,name='message_detil'),
    path('book_list/',login_required(views.book_list),name='book_list'),
    path('book_list1/',login_required(views.book_list1),name='book_list1'),
    path('delete/',views.delete,name='delete'),
    path('retrieve1/', views.retrieve1, name="retrieve1"),  # 检索
#    path('book_add/',views.book_add,name='book_add'),
#    path('book_remove/',views.book_remove,name='book_remove'),

    # path('',views.index,name='index'),
    # path('project_detail/<int:a>',views.project_detail,name='project_detail')

    # url(r'^$',views.index,name='index'),
    # url(r'^Project_detail/(?P<project_pk>[0-9]+)/$',views.project_detail,name='project_detail'),
]