from django.db import models


class Obrero(models.Model):
    """Empleado de la empresa."""

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.SmallIntegerField()

    def __str__(self):
        return f"{self.apellido} {self.nombre}"


class Ingeniero_en_jefe(models.Model):
    """Jefe de seccion de la empresa."""

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.SmallIntegerField()

    def __str__(self):
        return f"{self.apellido} {self.nombre}"

    class Meta:
        verbose_name = "Ingeniero "
        verbose_name_plural = "Ingenieros "


class Seccion(models.Model):
    """Area de trabajo de los empleados."""

    nombre = models.CharField(max_length=20, unique=True)
    obrero = models.ForeignKey(
        Obrero,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Obrero",
    )
    ingeniero = models.ForeignKey(
        Ingeniero_en_jefe,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Ingeniero ",
    )

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Seccion"
        verbose_name_plural = "Secciones"
