from django import forms

from procurement_app.models import ProcurementOfferModel


class ProcurementOfferForm(forms.ModelForm1):

    class Meta: 
        model = ProcurementOfferModel
        fields = [
            'product_name',
            'product_quantity',
            'product_price_per_unit',
            'issue_date'

        ]