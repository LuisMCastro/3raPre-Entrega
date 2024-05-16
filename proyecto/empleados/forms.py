from django import forms

from . import models


class SeccionForm(forms.ModelForm):
    class Meta:
        model = models.Seccion
        fields = ["nombre", "obrero", "ingeniero"]
