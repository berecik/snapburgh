from rest_framework import serializers

from .models import SnapGallery
from apps.snaps.serializers import SnapSerializer


class SnapGallerySerializer(serializers.ModelSerializer):

    snaps = SnapSerializer(many=True)

    class Meta:
        model = SnapGallery
        fields = '__all__'
