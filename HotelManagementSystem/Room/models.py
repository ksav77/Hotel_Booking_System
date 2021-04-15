from django.db import models
from django.conf import settings

# Create your models here.

class Room(models.Model):#inherited from models.model
    ROOM_CATEGORIES = {
        ('YAC','AC'),
        ('NAC','NON-AC'),
        ('KIN','KING'),
        ('QUE','QUEEN'),
    }
    roomnumber = models.IntegerField()
    category = models.CharField(max_length=3,choices=ROOM_CATEGORIES)
    beds = models.IntegerField()
    capacity = models.IntegerField()

    def __str__(self):
        return f'{self.roomnumber}. {self.category} with {self.beds} beds for {self.capacity} people'

class ImagePost(models.Model):
    caption = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    image = models.FileField(upload_to='db.sqlite3', blank = True)#%y for year#file will be saved to MEDIA_ROOT / img / 2021#Media_root is for server path to store files in the computer.

    def __str__(self):
      return self.caption        
