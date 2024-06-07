from django.db import models

# Create your models here.

class Smolensk(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/')

    def __str__(self):
        return self.title


class Sights(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/')

    def __str__(self):
        return self.title

class Routes(models.Model):
    routes = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/')

    def __str__(self):
        return self.title