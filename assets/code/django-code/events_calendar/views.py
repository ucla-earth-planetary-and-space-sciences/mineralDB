from django.views.generic import DetailView, ListView
from django.http import HttpResponseRedirect
from .models import *
from courses.models import Quarter


class SeminarCategoryListView(ListView):
    model = SeminarCategory
    template_name = "../templates/events_calendar/seminar-category-index.html"

    def get(self, request, *args, **kwargs):
        self.quarter = Quarter.objects.get(is_archive=False)
        self.queryset = SeminarCategory.objects.filter(quarter=self.quarter)
        return super(SeminarCategoryListView, self).get(request, *args, **kwargs)


class SeminarCurrent(ListView):
    model = SeminarCategory
    template_name = "../templates/events_calendar/seminar-events-index.html"

    def get(self, request, *args, **kwargs):
        self.category = SeminarCategory.objects.get(slug=kwargs.get('category'))
        self.active_quarter = Quarter.objects.get(is_visible=True, is_archive=False)
        self.queryset = SeminarEvent.objects.filter(seminar_category_id=self.category.id,
                                                    quarter_id=self.active_quarter.id).order_by('-year'),
        return super(SeminarCurrent, self).get(request, *args, **kwargs)


class SeminarCategoryView(ListView):
    model = SeminarEvent
    template_name = "../templates/events_calendar/seminar-events-index.html"

    def get(self, request, *args, **kwargs):
        self.quarter = Quarter.objects.get(slug=kwargs.get('quarter'))
        self.category = SeminarCategory.objects.get(slug=kwargs.get('category'))
        self.queryset = SeminarEvent.objects.filter(quarter_id=self.quarter, seminar_category_id=self.category.id)
        return super(SeminarCategoryView, self).get(request, *args, **kwargs)


class SeminarDetailView(DetailView):
    model = SeminarEvent
    template_name = "../templates/events_calendar/seminar-events-detail.html"
    context_object_name = 'seminar'
    pk_url_kwarg = 'id'


class ArchiveView(ListView):
    model = Quarter
    template_name = "../templates/events_calendar/seminar-quarter-index.html"

    def get(self, request, *args, **kwargs):
        self.category = kwargs.get('category')

        self.ok_quarters = SeminarEvent.objects.filter(seminar_category=self.category)
        self.quarter_list1 = []
        for each in self.ok_quarters:
            if each.quarter not in self.quarter_list1:
                self.quarter_list1.append(each.quarter)
            else:
                pass

        self.queryset = Quarter.objects.filter(is_visible=True).order_by('-year', 'season'),

        return super(ArchiveView, self).get(request, *args, **kwargs)

