from django import forms

from application.models import Image


class ImageForm(forms.ModelForm):
    class Meta:
        model=Image
        fields='__all__'
