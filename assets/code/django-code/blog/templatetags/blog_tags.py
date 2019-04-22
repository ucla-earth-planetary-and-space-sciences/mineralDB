from django import template
from blog.models import *

register = template.Library()


@register.inclusion_tag('blog/recent_stories.html', takes_context=True)
def get_recent_stories(context):
    recent_stories = Entry.objects.filter(publish=True).order_by('published').reverse()[:5]
    return {'recent_stories': recent_stories, }


@register.inclusion_tag('blog/featured_stories.html', takes_context=True)
def get_featured_stories(context):
    featured_stories = Entry.objects.filter(category__name='Featured').order_by('published').reverse()[:5]
    return {'featured_stories': featured_stories, }
