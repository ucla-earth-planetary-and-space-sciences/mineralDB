from django.db import models
from directory.models import DepartmentMember
from django.core.urlresolvers import reverse


# Create your models here.
class ResearchArea(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='uploads/images/research_areas/',
                              default='static/main/images/research_area.png')
    details = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    faculty = models.ManyToManyField(DepartmentMember, verbose_name="Faculty Members")
    banner = models.ImageField(upload_to='uploads/images/research_areas/', blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Research Area'
        verbose_name_plural = 'Research Areas'

    def get_absolute_url(self):
        return reverse('research-area-detail', args=[self.slug])
