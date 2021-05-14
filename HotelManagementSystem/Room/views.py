from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView
from .models import ImagePost, HomeImage, contact, FoodImage
from Room.models import Bookform
# Create your views here.


def home(request): 
    pics = HomeImage.objects.all()
    return render(request,'room/home.html',{"pics":pics})

def rooms(request):
    pics = ImagePost.objects.all()
    return render(request, 'room/rooms.html',{"pics":pics})#we pass django variable as third argument whose key(pics) contains dictionary of data.

def food(request):
    pics = FoodImage.objects.all()
    return render(request, 'room/food.html',{"pics":pics})#we pass django variable as third argument whose key(pics) contains dictionary of data.   
    
def about(request):
    return render(request,'room/aboutus.html')  

def cont(request):
    return render(request,'room/continue.html')      

def details(request, image_id):

    if request.method=="POST":
        fullname = request.POST['fullname']
        contact = request.POST['contact']
        room = request.POST['room']
        checkin = request.POST['checkin']
        checkout = request.POST['checkout']
        print(fullname, contact, room, checkin, checkout)
        ins = Bookform(fullname=fullname, contact=contact,room=room,checkin=checkin,checkout=checkout)
        ins.save()

    theta_image = get_object_or_404(ImagePost, pk=image_id)#get_object_or_404 get objects based on primary key,each objects in databse has number assigned to primary key
   
    return render(request, 'room/detail.html',{"theta_image":theta_image})
   

def Contact(request):
    if request.method == "POST":
        fname = request.POST.get('fname') 
        lname = request.POST.get('lname')
        Contactnumber = request.POST.get('Contactnumber')
        message = request.POST.get('message')
        print(fname,lname,Contactnumber,message)
        Contact = contact(fname = fname,lname = lname,Contactnumber = Contactnumber,message = message )
        Contact.save()
    return render(request,'room/Contact.html')
