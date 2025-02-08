
from django.contrib import admin
from django.urls import path
import taches.views as views

urlpatterns = [
    path('', views.index, name='home' ),
    path('add-collection', views.add_collection, name='add-collection' ),
    path('add-tache/', views.add_tache, name='add-tache' ),
    path('get-taches/<int:collection_pk>/', views.get_taches, name='get-taches' ),
    path('delete-tache/<int:tache_pk>/', views.delete_tache, name='delete-tache' ),
    path('delete-collection/<int:collection_pk>/', views.delete_collection, name='delete-collection' ),
    path('admin/', admin.site.urls),
]
