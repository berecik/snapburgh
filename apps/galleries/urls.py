from django.urls import path

from .views import gallery_ticket
from .views import SnapGalleryView

urlpatterns = [
    path('ticket/', gallery_ticket, name='gallery-ticket'),
]
