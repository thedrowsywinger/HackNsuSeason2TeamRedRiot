from django.shortcuts import render, redirect

from company_A_app.models import CompanyAInventoryModel, ProfileModel

from company_A_app.forms import CompanyAInventoryForm

# Create your views here.

def DashboardView(request):

    return render(request, "company_A_app/dashboard.html")


def InventoryView(request):

    if 'adding_product' in request.POST:
        incoming_data = {
            'product_name': request.POST['product_name'],
            'product_unit': request.POST['product_unit'],
            'product_quantity': request.POST['product_quantity'],
            'product_price_per_unit': request.POST['product_price_per_unit']
        }

    return render(request, "company_A_app/inventory.html")