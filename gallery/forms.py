from django import forms
from .models import GalleryImage

class GalleryImageForm(forms.ModelForm):
    class Meta:
        model = GalleryImage
        fields = (
            'image',
            'title',
            'tags',
        )
