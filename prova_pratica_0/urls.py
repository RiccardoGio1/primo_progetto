from django.urls import path
from prova_pratica_0.views import index3,somma,media

#RICORDO SEMPRE DI IMPORTARE DA PRIMA APP
app_name="prova_pratica_0"
urlpatterns=[
    path('somma', somma, name='somma'),
    path('media',media, name='media'),
    path('', index3, name='index3'),     
]