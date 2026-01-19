from django.urls import path
from .views import home, articoloDetailView,index4,listaArticoli

app_name='news'
urlpatterns = [
    path("home", home, name="homeview"),
    path("articoli/<int:pk>", articoloDetailView, name="articolo_detail"),
    path("lista_articoli/<int:pk>", listaArticoli, name="lista_articoli"),
    path('',index4,name='index4'),
]


