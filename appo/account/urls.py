from django.conf.urls import url
from django.urls import path, include
from .import views

app_name = 'account'
urlpatterns = [
    path('login',views.login,name="login"),

    path('user',views.user,name="user"),

    path('enroll',views.enroll,name="enroll"),

    path('test',views.test,name="test"),

    path('customer',views.customer,name="customer"),

    path('technician',views.technician,name="technician"),

    #path('Work1-1/',views.Work1-1,name='Work1-1'),
]