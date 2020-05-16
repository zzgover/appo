from django.conf.urls import url
from django.urls import path, include
from .import views
from django.contrib.auth.decorators import login_required

app_name = 'account1'
urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('user_center_userinfo/', login_required(views.UserInfoView.as_view()), name='userinfo'),
    path('user_center_book/',login_required(views.UserBookView.as_view()), name='userbook'),
]