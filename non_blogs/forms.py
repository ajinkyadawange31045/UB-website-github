from django import forms
from django.contrib.auth.models import User
from non_blogs.models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email','subject', 'content')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your full name'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email ID'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter subject to be discussed on..'}),
            'content': forms.Textarea(attrs={'class': 'form-control md-textarea', 'placeholder': 'Explain in brief..'}),
        }

