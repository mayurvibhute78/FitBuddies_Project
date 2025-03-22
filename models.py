from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=200,default=None)
    phone = models.CharField(max_length=50,default=None)
    email = models.EmailField(default=None)
    height = models.CharField(max_length=50,default=None)
    width = models.CharField(max_length=50,default=None)
    age =models.CharField(max_length=50,default=None)
    goal = models.CharField(max_length=50,default=None)
    message = models.CharField(max_length=50,default=None)

    def __str__(self):
        return self.name