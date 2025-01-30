from html import escape
from django.http import HttpResponse
from django.shortcuts import render, redirect

from taches.models import Collection

# Create your views here.

def index(request):
    """index page"""
    context = {}

    context["collections"] = Collection.objects.order_by("name")

    return render(request, 'taches/index.html', context=context)


def add_collection(request):
    """ajouote collection page"""
    collection_name = escape(request.POST.get("collection-name"))
    collection, created = Collection.objects.get_or_create(name=collection_name)

    if not created:
        return HttpResponse("La collection existe deja.")
    
    return redirect('home') 
