from django.contrib import admin
from django.urls import path
from . import views
#from .views import RoomList, BookingList
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', views.home, name='blog-home'),  #views.home vaneko views ko home function 
    path('room/', views.rooms, name='blog-room'), 
    path('aboutus/',views.about,name='blog-about'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)#we add this because every media and image has unique url

urlpatterns += staticfiles_urlpatterns()    