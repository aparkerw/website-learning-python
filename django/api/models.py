from django.db import models

# Create your models here.
class Record(models.Model):
    code = models.CharField(max_length=8, default="", unique=True)
    value = models.IntegerField()
    