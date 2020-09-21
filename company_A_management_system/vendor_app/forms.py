from django import forms
from vendor_app.models import proposalModel

class proposalModelForm(forms.Form):

    class Meta:
        model : proposalModel
        fields = [
            'vendor_name',
            'vendor_email'
            'vendor_mob',
            'vendor_address',
            'vendor_quantity',
            'vendor_price',
            'vendor_info',
            'product_id',
        ]
