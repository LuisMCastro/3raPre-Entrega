from django.urls import path

from home.views import base, index

app_name = "home"

urlpatterns = [
    path("", index, name="index"),
    path("base/", base, name="base"),
]
