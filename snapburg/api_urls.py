from rest_framework import routers

from apps.galleries.views import SnapGalleryViewSet
from apps.snaps.views import SnapViewSet

# Routers provide an easy way of automatically determining the URL conf.
rest_api_router = routers.DefaultRouter()
rest_api_router.register(r'galleries', SnapGalleryViewSet, basename="gallery")
rest_api_router.register(r'snaps', SnapViewSet, basename="snap")
