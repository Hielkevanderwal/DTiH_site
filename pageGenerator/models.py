from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ppg_data(models.Model):
    id = models.BigAutoField(unique=True, primary_key=True)
    data = models.JSONField()
    person = models.ForeignKey(User, on_delete=models.CASCADE)
