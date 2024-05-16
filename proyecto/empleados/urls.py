from django.urls import path

from . import views

app_name = "empleados"

urlpatterns = [
    path("lista/", views.seccion_list, name="seccion_list"),
    path("crear/", views.seccion_create, name="seccion_create"),
]
