from django.test import TestCase
from collection.models import Specimen


class SpecimenTests(TestCase):

    def create_specimen(self, name="TEST SPECIMEN", collection_id="0001", origin_local="TEST LOCATION",
                        chemistry="forumla", provenance="TEST PROVENANCE LOCATION",
                        dana_classification="001.001.001.001", external_link='https://test.link.location.com'):
        return Specimen.objects.create(name=name, collection_id=collection_id, origin_local=origin_local,
                                       chemistry=chemistry, provenance=provenance,
                                       dana_classification=dana_classification, external_link=external_link)

    def test_specimen_creation(self):
        test_model_instance = self.create_specimen()
        self.assertTrue(isinstance(test_model_instance, Specimen))
        self.assertEqual(test_model_instance.__str__(), test_model_instance.name)

