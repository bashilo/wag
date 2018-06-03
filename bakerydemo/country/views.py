# -*- coding: utf-8 -*-
from dal import autocomplete

from .models import Country,Province


class CountryAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return Country.objects.none()

        qs = Country.objects.all()

        if self.q:
            qs = qs.filter(name__icontains=self.q)

        return qs
class ProvinceAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return Province.objects.none()

        qs = Province.objects.all()

        if self.q:
            qs = qs.filter(name__icontains=self.q)

        return qs