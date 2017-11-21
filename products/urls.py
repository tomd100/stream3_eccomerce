from django.conf.urls import url
from django.contrib import admin

from accounts.views import get_index
from products.views import all_products


urlpatterns = [
    url(r"^$", all_products, name="all_products"),
]