from django.urls import path
from seconda_app.views import es_if,es_for,index,es_if_else_elif

#RICORDO SEMPRE DI IMPORTARE DA PRIMA APP
app_name="seconda_app"
urlpatterns=[
    path('es_if', es_if, name='es_if'),
    path('es_for', es_for, name='es_for'),
    path('es_if_else_elif',es_if_else_elif, name='es_if_else_elif'),
    path('',index,name='index2'),
]