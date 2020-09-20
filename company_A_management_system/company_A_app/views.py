from django.shortcuts import render, redirect

from company_A_app.models import CompanyAInventoryModel, ProfileModel

from company_A_app.forms import CompanyAInventoryForm

# Create your views here.

def DashboardView(request):

    profile = ProfileModel.objects.get(user=request.user)
    
    context = {
        'profile': profile,
    }

    return render(request, "company_A_app/dashboard.html", context)


def InventoryView(request):

    profile = ProfileModel.objects.get(user=request.user)

    if 'adding_product' in request.POST:
        print("Am I here")

        incoming_data = {
                'product_name': request.POST['product_name'],
                'product_unit': request.POST['product_unit'],
                'product_quantity': request.POST['product_quantity'],
                'product_price_per_unit': request.POST['product_price_per_unit'],
                'product_id': request.POST['product_id']
            }

        print(incoming_data)

        incoming_info = CompanyAInventoryForm(incoming_data)

        if CompanyAInventoryModel.objects.all().count() == 0:

            if incoming_info.is_valid():
                print("First time")
                model = CompanyAInventoryModel(
                    product_name = request.POST['product_name'],
                    product_unit = request.POST['product_unit'],
                    product_price_per_unit = request.POST['product_price_per_unit'],
                    product_quantity = request.POST['product_quantity'],
                    product_added_by = profile,
                    product_id = request.POST['product_id'],
                    company_a_product_id = 1

                )
                model.save()

            else:
                print(incoming_info.errors)

        else:

            current_product_id = CompanyAInventoryModel.objects.all().count() + 1

            if incoming_info.is_valid():
                print("there is history")
                model = CompanyAInventoryModel(
                    product_name = request.POST['product_name'],
                    product_unit = request.POST['product_unit'],
                    product_price_per_unit = request.POST['product_price_per_unit'],
                    product_quantity = request.POST['product_quantity'],
                    product_added_by = profile,
                    company_a_product_id = current_product_id

                )
                model.save()

            else:
                print(incoming_info.errors)


    return render(request, "company_A_app/inventory.html")