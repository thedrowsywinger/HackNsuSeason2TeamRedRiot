from django.shortcuts import render

from random import randint

from procurement_app.models import ProcurementOfferModel, AcceptedOfferModel
from company_A_app.models import CompanyAInventoryModel
from vendor_app.models import proposalModel

from procurement_app.forms import ProcurementOfferForm

from django.http import HttpResponse

# Create your views here.

def CreateProcurementOfferView(request):

    products = CompanyAInventoryModel.objects.all()

    if 'offer_submission' in request.POST:

        print("Creating a procurement offer")

        incoming_data = {
            'product_name': request.POST['product_name'],
            'product_quantity': request.POST['product_quantity'],
            'product_price_per_unit': request.POST['product_price_per_unit']
            # 'due_date': request.POST['due_date'],
        }

        print(incoming_data)

        incoming_info = ProcurementOfferForm(incoming_data)

        if incoming_info.is_valid():
            print("valid")

            model = ProcurementOfferModel(
                    product_name = request.POST['product_name'],
                    product_quantity = request.POST['product_quantity'],
                    product_price_per_unit=request.POST['product_price_per_unit'],
                    due_date = request.POST['due_date'],
                )
            model.save()

            # unique_code = randint(10000, 99999)

    proc_offers = ProcurementOfferModel.objects.all()

    context = {
        'products': products,
        'proc_offers': proc_offers
    }

    return render(request, 'procurement_app/create_procurement_offer.html', context)



def OffersForAProductView(request, product_id):
    print("Product ID: ", product_id)

    procurement_offer = ProcurementOfferModel.objects.get(company_a_proc_id=product_id)
    print(procurement_offer.product_name)

    vendor_offer = proposalModel.objects.filter(product_id=product_id)

    context = {

        'procurement_offer': procurement_offer,
        'vendor_offers': vendor_offer

    }

    return render(request, "procurement_app/vendor_offers_for_a_particular_product.html", context)


def AcceptingVendorOffer(request, proposal_id, product_id):

    print("Product ID: ", product_id)

    vendor_offer = proposalModel.objects.get(proposal_id=proposal_id)

    print("Proposal ID: ", proposal_id)

    proc_offer = ProcurementOfferModel.objects.get(company_a_proc_id=product_id)

    unique_code = randint(10000, 99999)

    if ProcurementOfferModel.objects.all().count() == 0:
        

        total_cost = (vendor_offer.vendor_price) * (vendor_offer.vendor_quantity)

        model = AcceptedOfferModel(
            due_date = proc_offer.due_date,
            vendor_unique_code = unique_code,
            offered_price_per_unit = vendor_offer.vendor_price,
            offered_quantity = vendor_offer.vendor_quantity,
            total_cost = total_cost,
            proc_offer = proc_offer
        )
        model.save()

        proc_offer.status = "Accepted"
        proc_offer.vendor_unique_code=unique_code
        proc_offer.save()

    else:
        
        current_unique_codes = []
        for i in ProcurementOfferModel.objects.all():
            current_unique_codes.append(i.vendor_unique_code)

        while(unique_code in current_unique_codes):
            unique_code = randint(10000, 99999)

        total_cost = (vendor_offer.vendor_price) * (vendor_offer.vendor_quantity)

        model = AcceptedOfferModel(
            due_date = proc_offer.due_date,
            vendor_unique_code = unique_code,
            offered_price_per_unit = vendor_offer.vendor_price,
            offered_quantity = vendor_offer.vendor_quantity,
            total_cost = total_cost,
            proc_offer = proc_offer
        )
        model.save()

        proc_offer.status = "Accepted"
        proc_offer.vendor_unique_code=unique_code
        proc_offer.save() 


    return HttpResponse("Request Accepted")