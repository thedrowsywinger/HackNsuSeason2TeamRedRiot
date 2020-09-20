from django.shortcuts import render

# Create your views here.
def offerView(request):
    return render(request, "vendor_app/procurement_offer.html")
