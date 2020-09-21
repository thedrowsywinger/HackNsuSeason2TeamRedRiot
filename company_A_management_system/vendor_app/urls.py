from django.urls import path, re_path
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

app_name = 'vendor_app'

from vendor_app.views import (

    offerView

)

urlpatterns = [

    path('procurement-offers/', offerView, name="offer"),
    # path('Inventory/', InventoryView, name="procurement")

]
