# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Snap


@admin.register(Snap)
class SnapAdmin(admin.ModelAdmin):
    list_display = ('id', 'photo', 'gallery', 'photo_thumbnail')
    list_filter = ('gallery',)


class SnapInlineAdmin(admin.StackedInline):
    model = Snap
