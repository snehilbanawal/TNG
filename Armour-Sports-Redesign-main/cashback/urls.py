from django.urls import path

from . import views
from accounts import views as acc_views

urlpatterns = [
    path('feedback/', views.feedback, name='feedback'),
    path('cashback/', views.cashback, name='cashback'),
    path('login/', views.login, name='login'),
    path('myprofile/', acc_views.userprofile, name='userprofile'),
    path('editprofile/', acc_views.edit_profile, name='editprofile'),
    path('signup/', views.signup, name='signup'),
    path('navbar/', views.navbar, name='navbar'),
    path('', views.home, name='home'),



]
