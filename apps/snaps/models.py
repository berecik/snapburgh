from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

from common.models import ChroniclerModel
from apps.galleries.models import SnapGallery


class Snap(ChroniclerModel):
    photo = models.ImageField(upload_to='photos')
    photo_thumbnail = ImageSpecField(source='photo',
                                     processors=[ResizeToFill(100, 50)],
                                     format='JPEG',
                                     options={'quality': 60})
    gallery = models.ForeignKey(SnapGallery, related_name="snaps", on_delete=models.CASCADE)

    @property
    def thumbnail(self):
        return self.photo_thumbnail.url

    def __str__(self):
        return self.photo.name
