from django.db import models
from company_A_app.models import ProfileModel   
from vendor_app.models import proposalModel

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


def payment_attachment_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/reference_number/<filename>
    return 'payment/{}/{}'.format(instance.vendor_unique_code, filename)


class AcceptedOfferDetailsModel(models.Model):

    due_date = models.DateField()
    vendor_unique_code = models.CharField(max_length=100)
    total_cost = models.FloatField()
    status = models.CharField(max_length=100, default="Ongoing")
    proc_offer = models.ForeignKey(ProcurementOfferModel, on_delete=models.CASCADE)
    vendor = models.ForeignKey(proposalModel, on_delete=models.CASCADE)
    paid_using = models.CharField(max_length=100, blank=True)
    paid_amount = models.CharField(max_length=100, blank=True)
    attachments = models.FileField(upload_to=payment_attachment_path, blank=True)
    paid_on = models.DateField()

    def __str__(self):
        return self.proc_offer.product_name


    