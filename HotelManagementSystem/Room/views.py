from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Room, ImagePost, HomeImage
# Create your views here.


def home(request): 
    pics = HomeImage.objects.all()
    return render(request,'room/home.html',{"pics":pics})

def rooms(request):
    pics = ImagePost.objects.all()
    return render(request, 'room/rooms.html',{"pics":pics})#we pass django variable as third argument which takes 
    
def about(request):
    return render(request,'room/aboutus.html')  

def cont(request):
    return render(request,'room/continue.html')      

def details(request, image_id):
    theta_image = get_object_or_404(ImagePost, pk=image_id)#get_object_or_404 get objects based on primary key,each objects in databse has number assigned to primary key
    return render(request, 'room/detail.html',{"theta_image":theta_image})


