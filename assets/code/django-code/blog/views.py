from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView
from datetime import date as date_function
from meta.views import Meta

from .models import Entry


class IndexView(ListView):
    template_name = 'blog/index.html'
    context_object_name = "news_list"
    #we might change this value a lot.
    paginate_by = 10

    def get_queryset(self):
        # here '-published' overrides the default behavior to show news items in reverse order (most recent first)
        return Entry.objects.filter(publish=True).order_by('-published', )


class EntryView(DetailView):
    template_name = 'blog/detail.html'
    model = Entry
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super(EntryView, self).get_context_data(**kwargs)
        context['meta'] = self.get_object().as_meta()

        return context
