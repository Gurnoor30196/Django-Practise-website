from django.db import models

# Create your models here.
#kinda blueprint
class Album(models.Model):
    # variablename
    artist = models.CharField(max_length=250)
album_title = models.CharField(max_length=550)
genre = models.CharField(max_length=100)
album_logo=models.CharField(max_length=1000)

class song(models.Model):
    album=models.ForeignKey(Album, on_delete=models.CASCADE) #delete related song on cascade if album is deleted.
    file_type=models.CharField(max_length=10)
    song_title=models.CharField(max_length=250)
    #migrations changes to database
    #noor qwerty123