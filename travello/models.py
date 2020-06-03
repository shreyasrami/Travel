from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class destination(models.Model):
    img  = models.ImageField(upload_to='pics')
    name = models.CharField(max_length=100)
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default = False)
    author = models.ForeignKey(default=None,to=User,on_delete=models.CASCADE)


    def __str__(self):
        return self.name
    