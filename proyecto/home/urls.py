from django.urls import path

from home.views import base, home_index

app_name = "home"

urlpatterns = [
    path("", home_index, name="home_index"),
    path("base/", base, name="base"),
]
