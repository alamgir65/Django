from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=40)
    Bio = models.TextField()
    Phone = models.CharField(max_length=11)
    
    def __str__(self):
        return self.name
    
