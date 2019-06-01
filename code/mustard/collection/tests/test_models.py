from django.test import TestCase
from collection.models import Specimen


class SpecimenTests(TestCase):

    def create_specimen(self, name="TEST SPECIMEN",collection_id="0001"):
        return Specimen.objects.create(name=name,collection_id=collection_id)

    def test_specimen_creation(self):
        test_model_instance = self.create_specimen()
        self.assertTrue(isinstance(test_model_instance,Specimen))
        self.assetEqual(test_model_instance.__str__(),test_model_instance.name)
