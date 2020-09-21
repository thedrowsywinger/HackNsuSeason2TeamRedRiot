from django.db import models

# Create your models here.
class proposalModel(models.Model):
    vendor_name = models.CharField(max_length=100)
    vendor_email = models.EmailField(max_length=100)
    vendor_mob = models.CharField(max_length=100)
    vendor_address = models.CharField(max_length=100)
    vendor_quantity = models.CharField(max_length=100)
    vendor_price = models.CharField(max_length=100)
    vendor_info = models.CharField(max_length=100)
    product_id = models.IntegerField()
    proposal_id = models.IntegerField()

    def __str__(self):
        return self.vendor_name
