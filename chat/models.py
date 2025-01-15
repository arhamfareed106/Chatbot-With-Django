from django.db import models

# Create your models here.


class Chat(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    
    
class Room(models.Model):
    name = models.CharField(max_length=100)
    label = models.SlugField(unique=True)

