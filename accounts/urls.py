from django.urls import path
from . import views

urlpatterns=[
   
    path("register/",views.register,name="register"),
    path("login",views.login,name="login"),
    path("logout",views.logout,name="logout"),
    path('register/login',views.login,name='login'),
    path('register/register',views.register,name='register')
    

]