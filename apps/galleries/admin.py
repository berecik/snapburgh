# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import SnapGallery
from apps.snaps.admin import SnapInlineAdmin


@admin.register(SnapGallery)
class SnapGalleryAdmin(admin.ModelAdmin):
    list_display = ('code',)
    list_filter = ('code',)
    inlines = (SnapInlineAdmin,)

