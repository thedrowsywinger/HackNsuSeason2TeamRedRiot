from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class ProfileModel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    company_email = models.CharField(max_length=250)
    company_role = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
