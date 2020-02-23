import uuid
from common.random_code import get_code

from django.db import models
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist

from django_global_request.middleware import get_request


class SnapGallery(models.Model):

    # This is secret key to find gallery
    key = models.UUIDField(primary_key=True, editable=False)

    class Meta:
        @property
        def next_gallery(cls):
            gallery = cls()
            gallery.save()
            return gallery

    def __init__(self):
        super().__init__()
        self.full_url = self.get_url()

    @classmethod
    def is_key_unique(cls, key):
        return cls.objects.filter(key=key).count() == 0

    def url_for_code(self, code):
        request = get_request()
        url = reverse('snapburg-gallery', kwargs={'code': code})
        self.url = url
        if request is not None:
            url = request.build_absolute_uri(url)
        return url

    @classmethod
    def uuid_for_url(cls, url):
        return uuid.uuid5(uuid.NAMESPACE_URL, url)

    @classmethod
    def by_code(cls, code, queryset=None):
        _url = cls.url_for_code(code)
        _key = cls.uuid_for_url(_url)

        if queryset is None:
            queryset = cls.objects.all()
        try:
            return queryset.get(key=_key)
        except ObjectDoesNotExist:
            return None

    def get_url(self):

        def __gen_code():
            code = get_code(count=SnapGallery.objects.count())
            _url = self.url_for_code(code)
            _key = self.uuid_for_url(_url)
            if self.is_key_unique(key=_key):
                return _url, _key
            else:
                return __gen_code()

        url, key = __gen_code()
        self.key = key

        return url

    def get_absolute_url(self):
        if self.url:
            return self.url
        else:
            raise Exception("NO URL FOR GALLERY")

    def __str__(self):
        return self.key
