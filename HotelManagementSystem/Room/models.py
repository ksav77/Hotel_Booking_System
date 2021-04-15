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
