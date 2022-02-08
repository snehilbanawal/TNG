from django.urls import path

from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('cashback/',views.cashback,name='cashback'),
    path('login/',views.login,name='login'),
    path('signup/',views.register,name='signup'),
    path('navbar/',views.navbar,name='navbar'),
    path('alerts/',views.alerts,name='alerts'),


]
    
