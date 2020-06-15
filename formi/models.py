from django.db import models
from djongo import models
# Create your models here.
class sample_collection(models.Model):
    data=models.TextField()