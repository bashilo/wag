# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.db import models
from django.shortcuts import redirect, render

from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey

from taggit.models import Tag, TaggedItemBase

from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page, Orderable
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from wagtail.snippets.edit_handlers import SnippetChooserPanel

from bakerydemo.base.blocks import BaseStreamBlock
from wagtail.snippets.models import register_snippet


class Country(models.Model):

    name=models.CharField(
        max_length=50,
    )
    def __str__(self):
        return self.name

@register_snippet
class Province(models.Model):
    country = models.ForeignKey(Country,blank=True,null=True,on_delete=models.CASCADE)
    name=models.CharField(
        max_length=50,
    )
    panels = [
        FieldPanel('name', classname="col9"),
        FieldPanel('country', classname="col6"),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('name'),
    ]
    def __str__(self):
        return self.name

class City(models.Model):

    name=models.CharField(
        max_length=50,
    )
    country = models.ForeignKey(Country,blank=True,null=True,on_delete=models.CASCADE)
    province = models.ForeignKey(Province,blank=True,null=True,on_delete=models.CASCADE)
    def __str__(self):
        return self.name