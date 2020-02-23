from rest_framework import routers, serializers, viewsets
from apps.galleries.views import SnapGalleryViewSet

# Routers provide an easy way of automatically determining the URL conf.
rest_api_router = routers.DefaultRouter()
rest_api_router.register(r'galleries', SnapGalleryViewSet)
