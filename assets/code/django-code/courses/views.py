from django.shortcuts import render
from django.views.generic import ListView, DetailView
from courses.models import Quarter, Course


# Create your views here.

class QuarterListView(ListView):
    model = Quarter
    template_name = "courses/quarter-index.html"

    def get(self, request, *args, **kwargs):
        self.queryset = Quarter.objects.filter(is_visible=True).order_by('-year')
        self.current_quarter = Quarter.objects.filter(is_archive=False, is_visible=True)

        #self.queryset = Quarter.objects.filter(is_visible=True)
        return super(QuarterListView, self).get(request,*args,**kwargs)


class CourseListView(ListView):
    model = Course
    template_name = "courses/course-index.html"

    def get(self, request, *args, **kwargs):
        slug = kwargs.get('quarter')
        self.quarter = Quarter.objects.get(slug=slug)
        self.queryset = Course.objects.filter(quarter=self.quarter).filter(active=True,).order_by('quarter')
        return super(CourseListView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(CourseListView, self).get_context_data(**kwargs)
        # Add in the publisher
        context['quarter'] = self.quarter
        return context


class CourseDetailView(DetailView):
    model = Course
    template_name = "courses/course-detail.html"
    slug_url_kwarg = 'detail'

    def get(self, request, *args, **kwargs):
        slug = kwargs.get('quarter')
        self.quarter = Quarter.objects.get(slug=slug)
        self.queryset = Course.objects.filter(quarter=self.quarter)
        return super(CourseDetailView, self).get(request, *args, **kwargs)
#
#
