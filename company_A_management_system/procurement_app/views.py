from django.shortcuts import render

from random import randint

from procurement_app.models import ProcurementOfferModel, AcceptedOfferModel, AcceptedOfferDetailsModel
from company_A_app.models import CompanyAInventoryModel
from vendor_app.models import proposalModel

from procurement_app.forms import ProcurementOfferForm

from django.http import HttpResponse

from django.template.loader import render_to_string
from django.core.mail import send_mail, EmailMessage
from django.conf import settings


# Create your views here.

def CreateProcurementOfferView(request):

    products = CompanyAInventoryModel.objects.all()

    if 'offer_submission' in request.POST:

        print("Creating a procurement offer")

        incoming_data = {
            'product_name': request.POST['product_name'],
            'product_quantity': request.POST['product_quantity'],
            'product_price_per_unit': request.POST['product_price_per_unit'],
            # 'due_date': request.POST['due_date'],
        }

        print(incoming_data)

        incoming_info = ProcurementOfferForm(incoming_data)

        if incoming_info.is_valid():
            print("valid")

            product_id = CompanyAInventoryModel.objects.get(product_name=request.POST['product_name']).company_a_product_id

            model = ProcurementOfferModel(
                    product_name = request.POST['product_name'],
                    product_quantity = request.POST['product_quantity'],
                    product_price_per_unit=request.POST['product_price_per_unit'],
                    product_unit = request.POST['product_unit'],
                    due_date = request.POST['due_date'],
                    company_a_proc_id=product_id
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

        # model = AcceptedOfferModel(
        #     due_date = proc_offer.due_date,
        #     vendor_unique_code = unique_code,
        #     offered_price_per_unit = vendor_offer.vendor_price,
        #     offered_quantity = vendor_offer.vendor_quantity,
        #     total_cost = total_cost,
        #     proc_offer = proc_offer
        # )
        # model.save()

        model = AcceptedOfferDetailsModel(
            due_date = proc_offer.due_date,
            vendor_unique_code = unique_code,
            total_cost = total_cost,
            proc_offer = proc_offer,
            vendor=vendor_offer,
        )
        model.save()

        proc_offer.status = "Accepted"
        proc_offer.vendor_unique_code=unique_code
        proc_offer.save()

        mail_subject = 'Congratulations'
        message = render_to_string('procurement_app/accepted_offer_email.html', {
            'uid': unique_code,
        })
        to_email = vendor_offer.vendor_email
        email = EmailMessage(
                    mail_subject, message, to=[to_email]
        )
        print("The email being sent")
        print("Email will be sent to: ", vendor_offer.vendor_email)
        print(message)
        # email.send()

    else:
        
        current_unique_codes = []
        for i in ProcurementOfferModel.objects.all():
            current_unique_codes.append(i.vendor_unique_code)

        while(unique_code in current_unique_codes):
            unique_code = randint(10000, 99999)

        total_cost = (vendor_offer.vendor_price) * (vendor_offer.vendor_quantity)

        # model = AcceptedOfferModel(
        #     due_date = proc_offer.due_date,
        #     vendor_unique_code = unique_code,
        #     offered_price_per_unit = vendor_offer.vendor_price,
        #     offered_quantity = vendor_offer.vendor_quantity,
        #     total_cost = total_cost,
        #     proc_offer = proc_offer
        # )
        # model.save()

        model = AcceptedOfferDetailsModel(
            due_date = proc_offer.due_date,
            vendor_unique_code = unique_code,
            total_cost = total_cost,
            proc_offer = proc_offer,
            vendor=vendor_offer,
        )
        model.save()

        proc_offer.status = "Accepted"
        proc_offer.vendor_unique_code=unique_code
        proc_offer.save() 

        mail_subject = 'Congratulations'
        message = render_to_string('procurement_app/accepted_offer_email.html', {
            'uid': unique_code,
        })
        to_email = vendor_offer.vendor_email
        email = EmailMessage(
                    mail_subject, message, to=[to_email]
        )
        print("The email being sent")
        print(message)
        # email.send()



    return HttpResponse("Request Accepted")


def ProcurementOrderView(request, vendor_unique_code):

    print("Here: ", vendor_unique_code)

    accepted_offer = AcceptedOfferDetailsModel.objects.get(vendor_unique_code=vendor_unique_code)

    context = {
        'accepted_offer': accepted_offer
    }

    return render(request, 'procurement_app/procurement_order.html', context)