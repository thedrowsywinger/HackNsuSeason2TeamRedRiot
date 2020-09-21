from django.contrib import admin
from company_A_app.models import CompanyAInventoryModel, ProfileModel
from vendor_app.models import proposalModel
# Register your models here.
admin.site.register(CompanyAInventoryModel)
admin.site.register(ProfileModel)
admin.site.register(proposalModel)
