from django.urls import path

from . import views

app_name = "empleados"

urlpatterns = [
    path("seccion/listado/", views.seccion_list, name="seccion_list"),
    path("seccion/crear/", views.seccion_create, name="seccion_create"),
    path("seccion/borrar/<int:pk>", views.seccion_delete, name="seccion_delete"),
    path("seccion/modificar/<int:pk>", views.seccion_update, name="seccion_update"),
    path("ingenieros/listado/", views.ingeniero_list, name="ingeniero_list"),
    path("ingeniero/crear/", views.ingeniero_create, name="ingeniero_create"),
    path("ingeniero/borrar/<int:pk>", views.ingeniero_delete, name="ingeniero_delete"),
    path("ingeniero/modificar/<int:pk>", views.ingeniero_update, name="ingeniero_update"),
    path("ingeniero/detallar/<int:pk>", views.ingeniero_detail, name="ingeniero_detail"),
    path("obrero/crear/", views.obrero_create, name="obrero_create"),
    path("obreros/listado/", views.obrero_list, name="obrero_list"),
    path("obrero/borrar/<int:pk>", views.obrero_delete, name="obrero_delete"),
    path("obrero/modificar/<int:pk>", views.obrero_update, name="obrero_update"),
    path("obrero/detallar/<int:pk>", views.obrero_detail, name="obrero_detail"),
]
