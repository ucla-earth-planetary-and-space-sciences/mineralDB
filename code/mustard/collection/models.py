from django.db import models


class Specimen(models.Model):
    name = models.CharField(max_length=200)
    collection_id = models.CharField(max_length=100, default=None, blank=True, )
    origin_local = models.CharField(max_length=100, default=None, blank=True)
    chemistry = models.CharField(max_length=100, default=None, blank=True)
    provenance = models.CharField(max_length=100, default=None, blank=True)
    dana_classification = models.CharField(max_length=30, default=None, blank=True)
    external_link = models.CharField(max_length=100, default=None, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['collection_id']


#replicated from http://webmineral.com/danaclass.shtml#.XNUGtKZlCT8
# DANA_CLASS = (
#     ('01', 'Native Elements'),
#     ('02', 'Sulfides - Including Selenides and Tellurides'),
#     ('03', 'Sulfosalts'),
#     ('04', 'Simple Oxides'),
#     ('05', 'Oxides Containing Uranium and Thorium'),
#     ('06', 'Hydroxides and Oxides Containing Hydroxyl'),
#     ('07', 'Multiple Oxides'),
#     ('08', 'Multiple Oxides with Nb, Ta, and Ti'),
#     ('09', 'Anhydrous and Hydrated Halides'),
#     ('10', 'Oxyhalides and Hydroxyhalides'),
#     ('11', 'Halide Complexes; Alumino-fluorides'),
#     ('12', 'Compound Halides'),
#     ('13', 'Acid Carbonates'),
#     ('14', 'Anhydrous Carbonates'),
#     ('15', 'Hydrated Carbonates'),
#     ('16a', 'Carbonates - Hydroxyl or Halogen'),
#     ('16b', 'Carbonates - Hydroxyl or Halogen'),
#     ('17', 'Compound Carbonates'),
#     ('18', 'Simple Nitrates'),
#     ('19', 'Nitrates - Hydroxyl or Halogen'),
#     ('20', 'Compound Nitrates'),
#     ('21', 'Iodates - Anhydrous and Hydrated'),
#     ('22', 'Iodates - Hydroxyl or Halogen'),
#     ('23', 'Compound Iodates'),
#     ('24', 'Borates - Anhydrous'),
#     ('25', 'Anhydrous Borates Containing Hydroxyl or Halogen'),
#     ('26','Hydrated Borates Containing Hydroxyl or Halogen'),
#     ('27','Compound Borates'),
#     ('28','Anhydrous Acid and Sulfates'),
#     ('29','Hydrated Acid and Sulfates'),
#     ('30','Anhydrous Sulfates Containing Hydroxyl or Halogen'),
#     ('31','Hydrated Sulfates Containing Hydroxyl or Halogen'),
#     ('32','Compound Sulfates'),
#     ('33','Selenates and Tellurates'),
#     ('34','Selenites - Tellurites - Sulfites'),
#     ('35','Anhydrous Chromates'),
#     ('36','Compound Chromates'),
#     ('37','Anhydrous Acid Phosphates'),
#     ('38','Anhydrous Phosphates'),
#     ('39','Hydrated Acid Phosphates'),
#     ('40','Hydrated Phosphates'),
#     ('41','Anhydrous Phosphates Containing Hydroxyl or Halogen'),
#     ('42','Hydrated Phosphates Containing Hydroxyl or Halogen'),
#     ('43','Compound Phosphates'),
#     ('44','Antimonates'),
#     ('45','Acid and normal Antimonites, Arsenites and Phosphites'),
#     ('46','Basic or Halogen-Containing Antimonites, Arsenites and Phosphites'),
#     ('47','Vanadium Oxysalts'),
#     ('48','Anhydrous Molybdates and Tungstates'),
#     ('49','Basic and Hydrated Molybdates and Tungstates'),
#     ('50','Salts of Organic Acids and Hydrocarbons'),
#     ('51','Nesosilicate Insular SiO4 Groups Only'),
#     ('52','Nesosilicate Insular SiO4 Groups and O, OH, F, and H2O'),
#     ('53','Nesosilicate Insular SiO4 Groups and Other Anions of Complex Cations'),
#     ('54','Nesosilicate Borosilicates and Some Beryllosilicates'),
#     ('55','Sorosilicate Si2O7 Groups, Generally with No Additional Anions'),
#     ('56','Sorosilicate Si2O7 Groups and O, OH, F. and H2O'),
#     ('57','Sorosilicate Insular Si3O10 and Larger Noncyclic Groups'),
#     ('58','Sorosilicate Insular, Mixed, Single, and Larger Tetrahedral Groups'),
#     ('59','Cyclosilicate Three-Membered Rings'),
#     ('60','Cyclosilicate Four-Membered Rings'),
#     ('61','Cyclosilicate Six-Membered Rings'),
#     ('62','Cyclosilicate Eight-Membered Rings'),
#     ('63','Cyclosilicate Condensed Rings'),
#     ('64','Cyclosilicates'),
#     ('65','Inosilicate Single-Width Unbranched Chains, W=1'),
#     ('66','Inosilicate Double-Width Unbranched Chains, W=2'),
#     ('67','Inosilicate Unbranched Chains with W>2'),
#     ('68','Inosilicate Structures with Chains of More Than One Width'),
#     ('69','Inosilicate Chains with Side Branches or Loops'),
#     ('70','Inosilicate Column or Tube Structures'),
#     ('71','Phyllosilicate Sheets of Six-Membered Rings'),
#     ('72','Phyllosilicate Two-Dimensional Infinite Sheets with Other Than Six-Membered Rings'),
#     ('73','Phyllosilicate Condensed Tetrahedral Sheets'),
#     ('74','Phyllosilicate Modulated Layers'),
#     ('75','Tectosilicate Si Tetrahedral Frameworks'),
#     ('76','Tectosilicate Al-Si Framework'),
#     ('77','Tectosilicate Zeolite group'),
#     ('78','Unclassified silicates'),
#)