from django.urls import path, re_path
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from procurement_app.views import (

    CreateProcurementOfferView,
    OffersForAProductView,
    AcceptingVendorOffer,
    ProcurementOrderView,
    FinalizePaymentView

)

app_name="procurement_app"

urlpatterns = [

    path('Create-A-Procurement-Offer/', CreateProcurementOfferView, name="create_procurement_offer"),
    path('Offers/<str:product_id>', OffersForAProductView, name='particular_product_offers'),
    path('Accept-Offer/<str:proposal_id>/<str:product_id>/', AcceptingVendorOffer, name='accepting_offer'),
    path('Order-View/<str:vendor_unique_code>/', ProcurementOrderView, name="order_view"),
    path('Finalize-Payment/<str:vendor_unique_code>/', FinalizePaymentView, name="payment")

]