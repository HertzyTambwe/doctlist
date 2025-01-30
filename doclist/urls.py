
from django.contrib import admin
from django.urls import path
import taches.views as views

urlpatterns = [
    path('', views.index, name='home' ),
    path('add-collection', views.add_collection, name='add-collection' ),
    path('add-tache', views.add_tache, name='add-tache' ),
    path('admin/', admin.site.urls),
]
