from django.test import TestCase
from .models import Zantta


class ZanttaModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Zantta.objects.create(title='first zantta')
        Zantta.objects.create(description='a description here')

    def test_title_content(self):
        zantta = Zantta.objects.get(id=1)
        expected_object_name = f'{zantta.title}'
        self.assertEquals(expected_object_name, 'first zantta')

    def test_description_content(self):
        zantta = Zantta.objects.get(id=2)
        expected_object_name = f'{zantta.description}'
        self.assertEquals(expected_object_name, 'a description here')