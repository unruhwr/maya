from django.db import models


# Create your models here.

class Picture(models.Model):
    picture_title = models.CharField(max_length=50)