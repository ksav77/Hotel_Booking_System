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

class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)#making user foreign key....on_delete=models.Cascade tells django to use the deleting effect i.e. continue deleting the dependent models as well.
    room = models.ForeignKey(Room,on_delete=models.CASCADE)#mathi Room class ko return message dekhaunxa
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()

    def __str__(self):
        return f'{self.user} has booked room no.{self.room} from {self.check_in} to {self.check_out}'


class Image(models.Model):
    caption = models.CharField(max_length=50)
    image = models.FileField(upload_to='db.sqlite3', blank = True)#%y for year#file will be saved to MEDIA_ROOT / img / 2021

    def __str__(self):
      return self.caption