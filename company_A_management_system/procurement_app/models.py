from django.db import models

# Create your models here.
class ProcurementOfferModel(models.Model):
    product_name = models.CharField(max_length=100)
    product_quantity = models.FloatField()
    product_price_per_unit = models.FloatField()
    status = models.FloatField()