from common.tests import RestApiTestCase

from .models import SnapGallery


class GallerySetUpTest(RestApiTestCase):

    @classmethod
    def setUpGalleryObject(cls):
        cls.gallery = SnapGallery()
        cls.galleryUrl = cls.gallery.get_url()
        cls.gallery.save()

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.setUpGalleryObject()


class GalleryTest(GallerySetUpTest):

    def test_string_representation(self):
        str()

