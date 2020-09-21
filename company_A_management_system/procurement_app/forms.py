from django import forms

from procurement_app.models import ProcurementOfferModel


class ProcurementOfferForm(forms.ModelForm):

    class Meta: 
        model = ProcurementOfferModel
        fields = [
            'product_name',
            'product_quantity',
            'product_price_per_unit',

        ]