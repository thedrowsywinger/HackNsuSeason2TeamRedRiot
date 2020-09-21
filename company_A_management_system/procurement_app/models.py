from django.db import models
from company_A_app.models import ProfileModel   

from datetime import datetime

# Create your models here.
class ProcurementOfferModel(models.Model):

    product_name = models.CharField(max_length=100)
    product_quantity = models.FloatField()
    product_unit = models.CharField(max_length=100)
    product_price_per_unit = models.FloatField()
    status = models.CharField(max_length=100, default="Pending")
    issue_date = models.DateField(default=datetime.now)
    vendor_unique_code = models.CharField(max_length=100, blank=True)
    # company_a_proc_id = models.CharField(max_length=100)

    def __str__(self):
        return self.product_name