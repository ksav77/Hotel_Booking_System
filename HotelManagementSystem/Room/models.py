from django.db import models
from django.conf import settings

# Create your models here.
class HomeImage(models.Model):
    caption = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    image = models.FileField(upload_to='db.sqlite3', blank = True)

    def __str__(self):
      return self.caption 

class ImagePost(models.Model):
    caption = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    image = models.FileField(upload_to='db.sqlite3', blank = True)#file will be saved to MEDIA_ROOT / db.sqlite3(pathname) / 2021#Media_root is for server path to store files in the computer.

    def __str__(self):
      return self.caption        

class contact(models.Model):
  fname = models.CharField(max_length=200)
  lname =  models.CharField(max_length=200)
  Contactnumber = models.BigIntegerField(max_length=10)
  message = models.TextField()

  def __str__(self):
      return self.fname

class FoodImage(models.Model):
    caption = models.CharField(max_length=50)
    price = models.CharField(max_length=200)
    image = models.FileField(upload_to='db.sqlite3', blank = True)#file will be saved to MEDIA_ROOT / db.sqlite3(pathname) / 2021#Media_root is for server path to store files in the computer.

    def __str__(self):
      return self.caption 

class Bookform(models.Model):
    fullname = models.CharField(max_length=30)
    contact = models.CharField(max_length=15)
    room = models.CharField(max_length=30)
    checkin = models.CharField(max_length=30)
    checkout = models.CharField(max_length=30)

    
    def __str__(self):
      return "Booked by"+" "+self.fullname     