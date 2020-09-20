from django.shortcuts import render

# Create your views here.

def CreateProcurementOfferView(request):

    
    return render(request, 'procurement_app/create_procurement_offer.html')