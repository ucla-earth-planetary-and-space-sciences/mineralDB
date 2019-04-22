from django import template
from research_areas.models import ResearchArea

register = template.Library()

@register.assignment_tag
def get_research_areas_list():
    research_areas_list = ResearchArea.objects.all()
    return research_areas_list