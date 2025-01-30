from django.shortcuts import render

# Create your views here.

def index(request):
    """index page"""
    return render(request, 'taches/index.html', context={})


