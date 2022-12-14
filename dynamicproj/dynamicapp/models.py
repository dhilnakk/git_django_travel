from django.db import models

# Create your models here.
class sites(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='imgs')
    desc=models.TextField()

    def __str__(self):
        return self.name
class Person(models.Model):
    fname = models.CharField(max_length=250)
    photo =models.ImageField(upload_to='pics')
    value = models.TextField()
    def __str__(self):
        return self.fname