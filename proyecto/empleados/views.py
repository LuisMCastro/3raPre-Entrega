from django.shortcuts import redirect, render

from empleados.forms import SeccionForm
from empleados.models import Seccion


def seccion_list(request):
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
