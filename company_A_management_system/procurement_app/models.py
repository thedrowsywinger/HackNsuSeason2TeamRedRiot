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
    due_date = models.DateField()
    vendor_unique_code = models.CharField(max_length=100, blank=True)
    company_a_proc_id = models.CharField(max_length=100)


    def __str__(self):
        return self.product_name

class AcceptedOfferModel(models.Model):

    due_date = models.DateField()
    vendor_unique_code = models.CharField(max_length=100)
    offered_price_per_unit = models.FloatField()
    offered_quantity = models.FloatField()
    total_cost = models.FloatField()
    status = models.CharField(max_length=100, default="Ongoing")
    proc_offer = models.ForeignKey(ProcurementOfferModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.proc_offer.product_name


    