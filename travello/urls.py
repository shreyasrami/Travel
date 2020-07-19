from django.urls import path
from . import views


urlpatterns=[
   
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('news',views.news,name='news'),
    path('td',views.td,name='td'),
    path('check',views.check,name='check')

]



