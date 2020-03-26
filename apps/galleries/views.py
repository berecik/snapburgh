# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

import datetime
import json

from django.db import transaction
from django.http import Http404
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils.translation import gettext as _
from django.views.generic import DetailView
from rest_framework import viewsets
from weasyprint import HTML
from weasyprint.fonts import FontConfiguration

from .models import SnapGallery
from .serializers import SnapGallerySerializer


# @login_required
def gallery_ticket(request):
    with transaction.atomic():
        ROWS = 7
        COLS = 2
        response = HttpResponse(content_type="application/pdf")
        response['Content-Disposition'] = "inline; filename={date}-cards.pdf".format(
            date=datetime.datetime.now().strftime('%Y-%m-%d'),
        )
        html = render_to_string("galleries/ticket/ticket.html", {
            'rows': (SnapGallery.galleries(COLS) for i in range(ROWS))
        })

        font_config = FontConfiguration()
        HTML(string=html).write_pdf(response, font_config=font_config)
        return response


class SnapGalleryViewSet(viewsets.ModelViewSet):
    queryset = SnapGallery.objects.all()
    serializer_class = SnapGallerySerializer


class SnapGalleryView(DetailView):
    model = SnapGallery

    def get_object(self, queryset=None):
        code = self.kwargs.get('code', None)
        if code is not None:
            obj = self.model.by_code(code, queryset=queryset)
            if obj is not None:
                return obj
        raise Http404(_("Gallery doesn't exist, so sorry!"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        serializer = SnapGallerySerializer(self.get_object())
        gallery_json = json.dumps(serializer.data)
        context["gallery"] = gallery_json
        return context
