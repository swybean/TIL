from django.db import models
from django.conf import settings

# Create your models here.

class Movie(models.Model):
    title = models.TextField(max_length=50)
    content = models.TextField(max_length=200)
    image = models.ImageField(blank=True, upload_to='movies/')

    def __str__(self):
        return self.title
    





