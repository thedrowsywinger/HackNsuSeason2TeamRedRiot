from django.urls import path, re_path
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from procurement_app.views import (

    CreateProcurementOfferView

)

app_name="procurement_app"

urlpatterns = [

    path('Create-A-Procurement-Offer/', CreateProcurementOfferView, name="create_procurement_offer")

]