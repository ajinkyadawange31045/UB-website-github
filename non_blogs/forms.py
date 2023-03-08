from django import forms
from django.contrib.auth.models import User
from non_blogs.models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email','subject', 'content')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'md-textarea'}),
        }

