from rest_framework import serializers
from .models import SnapGallery


class SnapGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = SnapGallery
        fields = '__all__'
