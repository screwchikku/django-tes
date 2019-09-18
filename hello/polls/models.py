from django.db import models

class Fruits(models.Model):
   name = models.CharField(max_length=200)
   image = models.ImageField(upload_to="uploads/",default ="image.jpg")
   price = models.IntegerField(default=0)
