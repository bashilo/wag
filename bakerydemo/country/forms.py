# -*- coding: utf-8 -*-
from dal import autocomplete

from django import forms
from bakerydemo.country import models

class CityForm(forms.ModelForm):
    class Meta:
        model = models.City
        fields = ('__all__')
        widgets = {
            'country': autocomplete.ModelSelect2(url='country-autocomplete'),
            'province': autocomplete.ModelSelect2(url='province-autocomplete')
        }
class ProvinceForm(forms.ModelForm):
    class Meta:
        model = models.Province
        fields = ('__all__')
        widgets = {
            'country': autocomplete.ModelSelect2(url='country-autocomplete'),
        }