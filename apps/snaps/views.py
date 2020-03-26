# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django.http import Http404
from django.utils.translation import gettext as _
from rest_framework import viewsets

from .models import Snap
from .serializers import SnapAllSerializer


class SnapViewSet(viewsets.ModelViewSet):
    queryset = Snap.objects.all()
    serializer_class = SnapAllSerializer
