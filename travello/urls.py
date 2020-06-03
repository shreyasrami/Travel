from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
   
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('news',views.news,name='news'),
    path('td',views.td,name='td'),
    path('check',views.check,name='check')



    
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)


