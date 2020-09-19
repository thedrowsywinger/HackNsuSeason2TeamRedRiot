from django.db import models

# Create your models here.

class CompanyAInventoryModel(models.Model):
    product_name = models.CharField(max_length=100)
    product_quantity = models.FloatField()
    product_unit = models.CharField(max_length = 50)
    product_price_per_unit = models.FloatField()

    def __str__(self):
        return self.product_name