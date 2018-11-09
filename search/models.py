from django.db import models


# Create your models here.
class Banks(models.Model):
    name = models.CharField(max_length=50)
    id = models.IntegerField(null=False)
    ifsc = models.CharField(max_length=11, primary_key=True, null=False)
    branch = models.CharField(max_length=74)
    address = models.CharField(max_length=195)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=26)

