from django import template
from courses.models import Quarter


register = template.Library()

#this tag should map the registrar's course listings to our current quarter here. Yes, this is a hacky way to do this, but its going to work as long as they dont change their URI formatting.


@register.assignment_tag
def get_class_links():
    current_quarter = Quarter.objects.get(is_archive=False, is_visible=True)

#this needs to be the logic to replace our quarters with the registrars abbreviations. really could use a case statemens
    year = str(current_quarter.year)

    if current_quarter.season == 1:
        class_links = year[2:]+'F'
    elif current_quarter.season == 3:
        class_links = year[2:] + 'S'
    elif current_quarter.season == 2:
        class_links = year[2:] + "W"
    elif current_quarter.season == 4:
        class_links = year[2:]+'1'
    else:
        class_links = "no match"
    out = 'https://sa.ucla.edu/ro/Public/SOC/Results?t='+str(class_links)+'&sBy=subject&sName=Earth%2C+Planetary%2C+and+Space+Sciences+%28EPS+SCI%29&subj=EPS+SCI&crsCatlg=Enter+a+Catalog+Number+or+Class+Title+%28Optional%29&catlg=&cls_no=&btnIsInIndex=btn_inIndex'
    return out


@register.assignment_tag
def get_ccle_links():
    current_quarter = Quarter.objects.get(is_archive=False, is_visible=True)

#this needs to be the logic to replace our quarters with the registrars abbreviations. really could use a case statemens
    year = str(current_quarter.year)

    if current_quarter.season == 1:
        class_links = year[2:]+'F'
    elif current_quarter.season == 3:
        class_links = year[2:] + 'S'
    elif current_quarter.season == 2:
        class_links = year[2:] + "W"
    elif current_quarter.season == 4:
        class_links = year[2:]+'1'
    else:
        class_links = "no match"
    out = 'https://ccle.ucla.edu/blocks/ucla_browseby/view.php?term='+str(class_links)+'&type=course&subjarea=EPS SCI'
    return out
