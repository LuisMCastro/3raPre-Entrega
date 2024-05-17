from django.shortcuts import redirect, render

from empleados.forms import IngenieroForm, ObreroForm, SeccionForm
from empleados.models import Ingeniero_en_jefe, Obrero, Seccion


def seccion_list(request):
    busqueda = request.GET.get("busqueda", None)
    if busqueda:
        print(busqueda)
        consulta = Seccion.objects.filter(nombre__icontains=busqueda)
    else:
        consulta = Seccion.objects.all()
    contexto = {"secciones": consulta}
    return render(request, "empleados/seccion_list.html", contexto)


def seccion_create(request):
    if request.method == "POST":
        form = SeccionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("empleados:seccion_list")
    else:
        form = SeccionForm()
    return render(request, "empleados/seccion_form.html", {"form": form})


def seccion_delete(request, pk: int):
    consulta = Seccion.objects.get(id=pk)
    if request.method == "POST":
        consulta.delete()
        return redirect("empleados:seccion_list")
    return render(request, "empleados/seccion_delete.html", {"object": consulta})


def seccion_update(request, pk: int):
    consulta = Seccion.objects.get(id=pk)
    if request.method == "POST":
        form = SeccionForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            return redirect("empleados:seccion_list")
    else:
        form = SeccionForm(instance=consulta)
    return render(request, "empleados/seccion_form.html", {"form": form})


def ingeniero_list(request):
    consulta = Ingeniero_en_jefe.objects.all()
    contexto = {"ingenieros": consulta}
    return render(request, "empleados/ingeniero_list.html", contexto)


def obrero_list(request):
    consulta = Obrero.objects.all()
    contexto = {"obreros": consulta}
    return render(request, "empleados/obrero_list.html", contexto)


def ingeniero_create(request):
    if request.method == "POST":
        form = IngenieroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("empleados:ingeniero_list")
    else:
        form = IngenieroForm()
    return render(request, "empleados/ingeniero_form.html", {"form": form})


def obrero_create(request):
    if request.method == "POST":
        form = ObreroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("empleados:obrero_list")
    else:
        form = ObreroForm()
    return render(request, "empleados/obrero_form.html", {"form": form})


def ingeniero_delete(request, pk: int):
    consulta = Ingeniero_en_jefe.objects.get(id=pk)
    if request.method == "POST":
        consulta.delete()
        return redirect("empleados:ingeniero_list")
    return render(request, "empleados/ingeniero_delete.html", {"object": consulta})


def obrero_delete(request, pk: int):
    consulta = Obrero.objects.get(id=pk)
    if request.method == "POST":
        consulta.delete()
        return redirect("empleados:obrero_list")
    return render(request, "empleados/obrero_delete.html", {"object": consulta})


def ingeniero_update(request, pk: int):
    consulta = Ingeniero_en_jefe.objects.get(id=pk)
    if request.method == "POST":
        form = IngenieroForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            return redirect("empleados:ingeniero_list")
    else:
        form = IngenieroForm(instance=consulta)
    return render(request, "empleados/ingeniero_form.html", {"form": form})


def obrero_update(request, pk: int):
    consulta = Obrero.objects.get(id=pk)
    if request.method == "POST":
        form = ObreroForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            return redirect("empleados:obrero_list")
    else:
        form = ObreroForm(instance=consulta)
    return render(request, "empleados/obrero_form.html", {"form": form})


def ingeniero_detail(request, pk: int):
    consulta = Ingeniero_en_jefe.objects.get(id=pk)
    contexto = {"ingeniero": consulta}
    return render(request, "empleados/ingeniero_detail.html", contexto)


def obrero_detail(request, pk: int):
    consulta = Obrero.objects.get(id=pk)
    contexto = {"obrero": consulta}
    return render(request, "empleados/obrero_detail.html", contexto)
