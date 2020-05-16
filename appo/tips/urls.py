from django.conf.urls import url
from django.urls import path, include
from .import views
from django.contrib.auth.decorators import login_required
app_name = 'tips'
urlpatterns = [
    path('comment/',login_required(views.comment),name='comment'),
    path('tips/',views.tips,name='tips'),


]