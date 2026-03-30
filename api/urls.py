from django import path
from .views import todos_view

urlpatterns = [
    path("todos/", todos_view,name="todos"),
]
