from django.db import models

class Demonstration(models.Model):

    name = models.CharField("name of the specimen", max_length=200)
    dana_classfication = models.CharField("DANA classification of specimen")
    origin = models.Charfield("origin/provenance of specimen")
    collection_id = models.Charfield("id number of specimen")
    chemistry = models.Charfield("chemical makeup of specimen")
    image = models.ImageField( blank=True)
    
    def __unicode__(self):
        return (self.name)
