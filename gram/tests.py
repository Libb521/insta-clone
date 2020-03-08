from django.test import TestCase
from .models import image, Profile, Comment, Likes

# Create your tests here.
class imageTestClass(TestCase):
    def setUp(self):
        self.