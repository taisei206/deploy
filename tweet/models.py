from django.db import models
# Create your models here.

class Post(models.Model):
    content = models.TextField()
    likes = models.IntegerField(default=0)
    SELECTION = [['happy','happy'],['sadness','sadness'],['horror','horror'],['SF','SF'],['other','other'],]
    selection = models.CharField(max_length=7, choices=SELECTION)

    def __str__(self):
        return self.content
    