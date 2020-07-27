import uuid

from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import RequestAborted
from django.db import models
from django.urls import reverse
from common.middleware import get_request

from common.random_code import get_code
from common.models import CreatedMixin


class SnapGallery(models.Model, CreatedMixin):
    # Secret key to find gallery
    code = models.CharField(max_length=8, primary_key=True, editable=False)

    class Meta:
        pass

    @classmethod
    def get_code(cls):
        """
        generate unique code for a new object
        :return: code value for a new gallery
        """
        code = get_code(count=cls.objects.count())
        if cls.is_unique(code=code):
            return code
        else:
            return cls.get_code()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.pk:
            self.code = self.get_code()

    @classmethod
    def galleries(cls, amount):
        for _ in range(amount):
            gallery = cls()
            yield gallery
            gallery.save()

    @property
    def url(self):
        return self.url_for_code(self.code)

    @classmethod
    def is_unique(cls, code):
        return not cls.objects.filter(code=code).exists()

    @classmethod
    def url_for_code(cls, code):
        request = get_request()
        url = reverse('snapburg-gallery', kwargs={'code': code})
        if request is not None:
            url = request.build_absolute_uri(url)
        return url

    @classmethod
    def by_code(cls, code, queryset=None):

        if queryset is None:
            queryset = cls.objects

        try:
            return queryset.get(code=code)
        except ObjectDoesNotExist:
            return None

    def get_absolute_url(self):
        return self.url

    def __str__(self):
        return self.url
