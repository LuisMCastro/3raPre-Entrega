from django.urls import path

from . import views

app_name = "empleados"

urlpatterns = [
    path("lista/", views.seccion_list, name="seccion_list"),
    path("crear/", views.seccion_create, name="seccion_create"),
    path("borrar/<int:pk>", views.seccion_delete, name="seccion_delete"),
    path("modificar/<int:pk>", views.seccion_update, name="seccion_update"),
]
