from django.shortcuts import render


def home_index(request):
    return render(request, "home/home_index.html")


def base(request):
    return render(request, "home/base.html")
