from django.db import models

# Create your models here.
class User(models.Model):
    f_name = models.CharField(max_length=50, unique = True)
    l_name = models.CharField(max_length=50, unique = True)
    email = models.CharField(max_length=50, unique = True)

    def __str__(self):
        return self.f_name
    
