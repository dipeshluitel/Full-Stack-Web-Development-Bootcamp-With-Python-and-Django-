from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=120)
    text = models.TextField()

    def __str__(self):
        return self.name

   
