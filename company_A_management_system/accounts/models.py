from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class ProfileModel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    company_email = models.CharField(max_length=250)
    company_role = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.first_name + " " + self.last_name)

