from django.db import models
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    Firstname = models.CharField(max_length=200)
    Lastname = models.CharField(max_length=200)
    Middlename = models.CharField(max_length=200)
    Username = models.CharField(max_length=200)
    Email = models.CharField(max_length=200)
    Password = models.CharField(max_length=200)
    Birthdate = models.CharField(max_length=200)

    def __str__(self):
        return self.Firstname
    
    def get_absolute_url(self):
        return reverse('detail', args=[str(self.pk)])