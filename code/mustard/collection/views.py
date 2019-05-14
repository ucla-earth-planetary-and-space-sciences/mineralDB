from collection.models import Specimen
from django.shortcuts import render, get_object_or_404

def collection_list(request):
    try:
        collection_list = Specimen.objects.all()
    except Specimen.DoesNotExist:
        raise Http404("Nothing in the Collection!")
    return render(request, 'collection_list.html', {'Collection': collection_list})

def collection_item(request):
    collection_item = get_object_or_404(Specimen, pk=1)
    return render(request, 'collection_detail.html', {'Specimen': collection_item})


def about(request):
    return render(request, 'about.html')

def home(request):
    return render(request, 'home.html')
