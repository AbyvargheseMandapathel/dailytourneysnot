from django.db import models

# Create your models here.

class BGMI (models.Model):
  name = models.CharField(max_length=50)
  link = models.CharField(max_length=500)
  img = models. ImageField(upload_to='pics')
  desc = models.TextField()
  price = models.IntegerField()