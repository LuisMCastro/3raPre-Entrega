from django import forms

from . import models


class SeccionForm(forms.ModelForm):
    class Meta:
        model = models.Seccion
        fields = ["nombre", "obrero", "ingeniero"]


class IngenieroForm(forms.ModelForm):
    class Meta:
        model = models.Ingeniero_en_jefe
        fields = ["nombre", "apellido", "edad"]


class ObreroForm(forms.ModelForm):
    class Meta:
        model = models.Obrero
        fields = ["nombre", "apellido", "edad"]
