from django.contrib import admin
from django.urls import path
from . import views
#from .views import RoomList, BookingList
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.site.site_header = "Annapurna Hotel"
admin.site.index_title = "Welcome to Annapurna Hotel Dashboard"

urlpatterns = [
    path('', views.home, name='blog-home'),  #views.home vaneko views ko home function 
    path('room/', views.rooms, name='blog-room'), 
    path('food/',views.food,name='blog-food'),
    path('aboutus/',views.about,name='blog-about'),
    path('Contact/',views.Contact,name='blog-Contact'),
    path('aboutuscontinue/',views.cont,name='blog-aboutcon'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)#we add this because every media and image has unique url

urlpatterns += staticfiles_urlpatterns()    