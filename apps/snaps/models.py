from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

from apps.galleries.models import SnapGallery


class Snap(models.Model):
    photo = models.ImageField(upload_to='photos')
    photo_thumbnail = ImageSpecField(source='photo',
                                      processors=[ResizeToFill(100, 50)],
                                      format='JPEG',
                                      options={'quality': 60})
    gallery = models.ForeignKey(SnapGallery, related_name="snaps", on_delete=models.CASCADE)
