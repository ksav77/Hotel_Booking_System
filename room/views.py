from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Room, Booking, Image
# Create your views here.

posts = [{
    'author':'herolal',
    'title': 'blog post 1',
    'content': 'first post content',
    'date_posted': 'august 4,2018'
},
    {
        'author':'queen',
        'title': 'blog post 2',
        'content': 'second post content',
        'date_posted': 'august 4,2018'
    }
]

def home(request):
    context = {
       'posted': posts
    }
    return render(request,'room/home.html', context)#we pass context of home pass as third argument whose key(posts) contains dictionary of data.
    

def rooms(request):
    pics = Image.objects.all()
    return render(request, 'room/rooms.html',{"pics":pics})#we pass django variable as third argument which takes dictionary
    return render(request, 'room/rooms.html')

class RoomList(ListView):
    model = Room

class BookingList(ListView):
    model = Booking