# -*- coding: utf-8 -*-
from .views import CountryAutocomplete,ProvinceAutocomplete
from django.conf.urls import  url

urlpatterns = [
    url(
        r'^country-autocomplete/$',
        CountryAutocomplete.as_view(create_field='name'),
        name='country-autocomplete',
    ),
    url(
        r'^province-autocomplete/$',
        ProvinceAutocomplete.as_view(create_field='name'),
        name='province-autocomplete',
    ),
]