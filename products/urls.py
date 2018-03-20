from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^products_list/', get_products_list, name='products_list'),
    ]
