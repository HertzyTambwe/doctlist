from html import escape
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.utils.text import slugify
from django.template.loader import render_to_string

from taches.models import Collection, Tache

# Create your views here.

def index(request):
    """index page"""
    context = {}
    collection_slug = request.GET.get("collection")
    collection = Collection.get_default_collection()

    if collection_slug:
        collection = get_object_or_404(Collection, slug=collection_slug)


    context["collections"] = Collection.objects.order_by("slug")
    context["taches"] = collection.tache_set.order_by("description")
    
    return render(request, 'taches/index.html', context=context)


def add_collection(request):
    """ajouote collection page"""
    collection_name = escape(request.POST.get("collection-name"))
    collection, created = Collection.objects.get_or_create(name=collection_name, slug=slugify(collection_name))

    if not created:
        return HttpResponse("La collection existe deja.", status=409)
    
    return HttpResponse(f'<h2>{collection_name}</h2>')

def add_tache(request):

    collection = Collection.objects.get(slug=request.POST.get("collection"))
    description = escape(request.POST.get("tache-description"))
    Tache.objects.create(description=description, collection=collection)
    return HttpResponse(description)


def get_taches(request, collection_pk):

    collection = get_object_or_404(Collection, pk=collection_pk)
    taches = collection.tache_set.order_by("description")
    return render(request, "taches/taches.html", context={"taches": taches})