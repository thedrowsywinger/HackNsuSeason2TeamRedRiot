from django.shortcuts import render, redirect

# Create your views here.

def DashboardView(request):

    return render(request, "company_A_app/dashboard.html")


def InventoryView(request):

    return render(request, "company_A_app/inventory.html")