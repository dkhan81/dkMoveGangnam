from django.db import models

# Create your models here.
from django.utils import timezone

class DkNote(models.Model) :
    name = models.CharField(max_length=30)
    text = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
    
    def __str__(self):
        return "{} : {}".format(self.name, self.text)



class Pk(models.Model) :
    dk_id = models.CharField(max_length=30, primary_key=True)
    name = models.CharField(max_length=30)
    text = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self
