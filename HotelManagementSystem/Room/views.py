from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Room, Image 
# Create your views here.


def home(request): 
    return render(request,'room/home.html')#we pass context of home pass as third argument whose key(posts) contains dictionary of data.
    

def rooms(request):
    pics = Image.objects.all()
    return render(request, 'room/rooms.html',{"pics":pics})#we pass django variable as third argument which takes 
    
def about(request):
    return render(request,'room/aboutus.html')    
   

