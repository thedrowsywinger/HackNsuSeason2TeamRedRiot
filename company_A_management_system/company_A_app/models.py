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

class CompanyAInventoryModel(models.Model):
    product_name = models.CharField(max_length=100)
    product_quantity = models.FloatField()
    product_unit = models.CharField(max_length = 50)
    product_price_per_unit = models.FloatField()
    product_added_by = models.ForeignKey(ProfileModel, on_delete=models.CASCADE)
    company_a_product_id = models.IntegerField()

    def __str__(self):
        return self.product_name