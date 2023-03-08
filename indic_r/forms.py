from django import forms
from .models import EntityComment

class EntityCommentForm(forms.ModelForm):
    class Meta:
        model = EntityComment
        fields = ('title', 'content',)
