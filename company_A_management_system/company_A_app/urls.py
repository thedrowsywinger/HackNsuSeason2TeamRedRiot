from django.urls import path, re_path
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from company_A_app.views import (

    DashboardView,
    InventoryView

)

app_name = 'company_A_app'

urlpatterns = [

    path('Dashboard/', DashboardView, name="dashboard"),
    path('Inventory/', InventoryView, name="inventory")

]
