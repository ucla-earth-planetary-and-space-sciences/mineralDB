from collection.models import Specimen
from django.shortcuts import render, get_object_or_404


def home(request):

    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def collection_list(request):
    try:
        collection_list = Specimen.objects.all()
    except Specimen.DoesNotExist:
        raise Http404("Nothing in the Collection!")
    return render(request, 'collection_list.html', {'specimens': collection_list})

def collection_item(request, item):
    collection_item = get_object_or_404(Specimen, pk=item)
    return render(request, 'collection_detail.html', {'specimen': collection_item})
