from django.contrib import admin
from django.urls import path
from . import views
from .views import RoomList, BookingList
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='blog-home'),  #views.home vaneko views ko home function 
    path('room/', views.rooms, name='blog-blog'), 
    path('roomlist/',RoomList.as_view(),name='RoomList'),#as_view method for class view method(RoomList is class so)
    path('bookinglist/',BookingList.as_view(),name='BookingList'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)#we add this because every media and image has unique url