from django.urls import path
from .views import view_a,view_b,view_c,view_d,index5

app_name='voti'
urlpatterns = [
    path("materie", view_a, name="materie"),
    path("StudentiConVoto",view_b,name="StudentiConVoto"),
    path("media_studenti",view_c,name="media_studenti"),
    path("Max_Min",view_d,name="Max_Min"),
    path('',index5,name='index5'),
]