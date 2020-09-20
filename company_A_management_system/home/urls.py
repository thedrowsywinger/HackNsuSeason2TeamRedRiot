from django.urls import path, re_path
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from home.views import (
    
    HomeView,
    SigningUpCompanyRepresentativesView,
    LoggingInCompanyRepresentativesView

)

app_name = 'home'

urlpatterns = [

    path('', HomeView, name='home'),
    path('Company-Representative-Sign-Up/', SigningUpCompanyRepresentativesView, name='signing_up'),
    path('Company-Representative-Log-In/', LoggingInCompanyRepresentativesView, name='logging_in'),

]