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
