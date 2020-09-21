from django import forms
from company_A_app.models import CompanyAInventoryModel, ProfileModel

class CompanyAInventoryForm(forms.ModelForm):

    class Meta:
        model= CompanyAInventoryModel
        fields = [
            'product_name',
            'product_unit',
            'product_quantity',
            'product_price_per_unit'
        ]
