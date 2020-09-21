from django.shortcuts import render
from procurement_app.models import ProcurementOfferModel
from vendor_app.models import proposalModel
from vendor_app.forms import proposalModelForm

from datetime import date

# Create your views here.
def offerView(request):
    procurement_list = ProcurementOfferModel.objects.all()
    
    # offer_expiring_list = []

    # for i in procurement_list:
    #     issue_date = i.issue_date
    #     current_date = date.today()
    #     delta = current_date-issue_date
    #     remaining = 7 - delta
    #     if remaining <= 0:
    #         remaining = 0
    #         offer_expiring_list.append(remaining)
    #     else:
    #         offer_expiring_list.append(remaining)




    proposal_id = proposalModel.objects.all().count() + 1
    if 'send_offer' in request.POST:
        incoming_data = {
            'vendor_name' : request.POST['vendor_name'],
            'vendor_email' : request.POST['vendor_email'],
            'vendor_mob' : request.POST['vendor_mob'],
            'vendor_address' : request.POST['vendor_address'],
            'vendor_quantity' : request.POST['vendor_quantity'],
            'vendor_price' : request.POST['vendor_price'],
            'vendor_info' : request.POST['vendor_info'],
            'product_id' : request.POST['product_id'],
            }

        incoming_info = proposalModelForm(incoming_data)

        if incoming_info.is_valid():
            model = proposalModel(
                vendor_name = request.POST['vendor_name'],
                vendor_email = request.POST['vendor_email'],
                vendor_mob = request.POST['vendor_mob'],
                vendor_address = request.POST['vendor_address'],
                vendor_quantity  = request.POST['vendor_quantity'],
                vendor_price = request.POST['vendor_price'],
                vendor_info = request.POST['vendor_info'],
                product_id = request.POST['product_id'],
                proposal_id = proposal_id

            )
            model.save()
        else:
            print("Error")
            return render(request, 'vendor_app/procurement_offer.html',{
            'error': incoming_info.errors,
            })
    return render(request, 'vendor_app/procurement_offer.html',{
    'products' : procurement_list,
    # 'offer_expiring_list': offer_expiring_list,
    })


# def track_offer(request):
#     code = ProcurementOfferModel.objects.all()
#     if 'trackerButton' in request.POST:
#         for i in code.id:
#             if(i == request.POST['tracker']):
#                 return render(request, 'home/home.html')
#     return render(request, "vendor_app/home.html")
