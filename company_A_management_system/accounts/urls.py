from django.urls import path, re_path
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from accounts.views import (

    SigningUpCompanyRepresentativesView,
    LoggingInCompanyRepresentativesView


)

app_name = 'accounts'

urlpatterns = [

    path('Company-Representative-Sign-Up/', SigningUpCompanyRepresentativesView, name='signing_up'),
    path('Company-Representative-Log-In/', LoggingInCompanyRepresentativesView, name='logging_in'),

]