from django.db import models
from django.contrib.auth.models import User


class SmokingAreaModel(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    attention=models.TextField()
    start_usage_time=models.TimeField()
    end_usage_time=models.TimeField()
    postdate=models.DateField(auto_now_add=True)
