# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import SnapGallery


@admin.register(SnapGallery)
class SnapGalleryAdmin(admin.ModelAdmin):
    list_display = ('key',)
