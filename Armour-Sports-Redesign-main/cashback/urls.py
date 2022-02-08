from django.urls import path

from . import views

urlpatterns = [
    path('feedback/',views.feedback,name='feedback'),
    path('cashback/',views.cashback,name='cashback'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('navbar/',views.navbar,name='navbar'),
    path('cashbackform', views.cashbackform, name='cashbackform'),
    path('feedbackform', views.feedbackform, name='feedbackform'),
   


]
    
