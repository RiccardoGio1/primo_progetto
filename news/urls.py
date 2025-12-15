from django.urls import path
from .views import home, articoloDetailView,index4

app_name='news'
urlpatterns = [
    path("", home, name="homeview"),
    path("articoli/<int:pk>", articoloDetailView, name="articolo_detail"),
    path('',index4,name='index4'),
]


