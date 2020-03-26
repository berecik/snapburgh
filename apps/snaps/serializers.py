from rest_framework import serializers

from .models import Snap


class SnapAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snap
        fields = '__all__'


class SnapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snap
        fields = ['id', 'photo', 'thumbnail']
