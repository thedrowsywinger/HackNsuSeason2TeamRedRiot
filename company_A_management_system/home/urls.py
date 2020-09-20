from django.urls import path, re_path
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from home.views import (
    
    HomeView,
    LogoutView,

)

app_name = 'home'

urlpatterns = [

    path('', HomeView, name='home'),
    path('logout/', LogoutView, name='logout')

]