import uuid
from django.test import TestCase
from .models import SnapGallery


class UserModelTest(TestCase):
    fixtures = ['users_test.json']

    def test_string_representation(self):
        gallery = SnapGallery()


