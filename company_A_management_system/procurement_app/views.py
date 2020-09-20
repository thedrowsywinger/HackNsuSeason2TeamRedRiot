from django.shortcuts import render

from random import randint

from procurement_app.models import ProcurementOfferModel
from company_A_app.models import CompanyAInventoryModel

from procurement_app.forms import ProcurementOfferForm

# Create your views here.

def CreateProcurementOfferView(request):

    products = CompanyAInventoryModel.objects.all()

    if 'offer_submission' in request.POST:

        print("Creating a procurement offer")

        incoming_data = {
            'product_name': request.POST['product_name'],
            'product_quantity': request.POST['product_quantity'],
            'product_price_per_unit': request.POST['product_price_per_unit'],
        }

        print(incoming_data)

        incoming_info = ProcurementOfferForm(incoming_data)

        if incoming_info.is_valid():
            print("valid")

            unique_code = randint(10000, 99999)
            
            if ProcurementOfferModel.objects.all().count() == 0:
                
                model = ProcurementOfferModel(
                    product_name = request.POST['product_name'],
                    product_quantity = request.POST['product_quantity'],
                    product_price_per_unit=request.POST['product_price_per_unit'],
                    vendor_unique_code = unique_code
                )
                # model.save()

            else:

                list_of_unique_codes_used = []
                for i in ProcurementOfferModels.objects.all():
                    list_of_unique_codes_used.append(i.vendor_unique_code)

                while(unique_code in list_of_unique_codes_used):
                    unique_code = randint(10000, 99999)

                
                model = ProcurementOfferModel(
                    product_name = request.POST['product_name'],
                    product_quantity = request.POST['product_quantity'],
                    product_price_per_unit=request.POST['product_price_per_unit'],
                    vendor_unique_code = unique_code
                )
                # model.save()



    context = {
        'products': products,
    }

    return render(request, 'procurement_app/create_procurement_offer.html', context)