from django.contrib import admin
from procurement_app.models import ProcurementOfferModel, AcceptedOfferModel,AcceptedOfferDetailsModel

# Register your models here.

admin.site.register(ProcurementOfferModel)
admin.site.register(AcceptedOfferModel)
admin.site.register(AcceptedOfferDetailsModel)