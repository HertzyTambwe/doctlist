from html import escape
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.utils.text import slugify
from django.template.loader import render_to_string

from taches.models import Collection, Tache

# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Collection

def index(request):
    """Index page"""
    collection_slug = request.GET.get("collection", "_default")

    if collection_slug == "_default":
        return redirect(f"{reverse('home')}?collection=_default")

    collection = get_object_or_404(Collection, slug=collection_slug)

    context = {
        "collections": Collection.objects.order_by("slug"),
        "collection": collection,
        "taches": collection.tache_set.order_by("description"),
    }

    return render(request, "taches/index.html", context)



def add_collection(request):
    """ajouote collection page"""
    collection_name = escape(request.POST.get("collection-name"))
    collection, created = Collection.objects.get_or_create(name=collection_name, slug=slugify(collection_name))

    if not created:
        return HttpResponse("La collection existe deja.", status=409)
    
    return render(request, "taches/collection.html", context={"collection": collection})

def add_tache(request):

    collection = Collection.objects.get(slug=request.POST.get("collection"))
    description = escape(request.POST.get("tache-description"))
    tache =Tache.objects.create(description=description, collection=collection)
    return render(request, "taches/tache.html", context={"tache": tache})


def get_taches(request, collection_pk):

    collection = get_object_or_404(Collection, pk=collection_pk)
    taches = collection.tache_set.order_by("description")
    return render(request, "taches/taches.html", context={"taches": taches, "collection": collection})

def delete_tache(request, tache_pk):
    tache = get_object_or_404(Tache, pk=tache_pk)
    tache.delete()
    return HttpResponse("")

def delete_collection(request, collection_pk):
    collection = get_object_or_404(Collection, pk=collection_pk)
    collection.delete()
    return redirect('home')
