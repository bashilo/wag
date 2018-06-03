# -*- coding: utf-8 -*-
from django.contrib import admin
from bakerydemo.country.models import Country,City,Province
from .forms import CityForm,ProvinceForm

class CityInline(admin.TabularInline):
    model = City
    form = CityForm

class CountryAdmin(admin.ModelAdmin):
    inlines = [CityInline,]


class CityAdmin(admin.ModelAdmin):
    form = CityForm
class ProvinceAdmin(admin.ModelAdmin):
    form = ProvinceForm
admin.site.register(Country, CountryAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Province, ProvinceAdmin)