from django.urls import path
from .views import home, articoloDetailView,index4,listaArticoli,queryBase,giornalistaDetailView

app_name='news'
urlpatterns = [
    path("home", home, name="homepage"),
    path("articoli/<int:pk>", articoloDetailView, name="articolo_detail"),
    path("lista_articoli/<int:pk>", listaArticoli, name="lista_articoli"),
    path("lista_articoli", listaArticoli, name="lista_articoli"),
    path("query_base", queryBase, name="query_base"),
    path("giornalista_detail/<int:pk>", giornalistaDetailView, name="giornalista_detail"),
    path('',index4,name='index4'),
    
]


