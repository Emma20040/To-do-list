from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    title= models.CharField(max_length=100)
    discription =models.TextField(max_length=500)
    image=models.ImageField(upload_to='images/')

    def __str__(self):

      return self.title

# Create your models here.
