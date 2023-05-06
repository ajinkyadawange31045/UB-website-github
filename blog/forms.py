from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,UserChangeForm
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from blog.models import Post_with_image,Author,Category,Comment
from non_blogs.models import Initiative, Value, Past_events, Advertisement, Youtube_Video
from mptt.forms import TreeNodeChoiceField

# comment form
class NewCommentForm(forms.ModelForm):
    parent = TreeNodeChoiceField(queryset=Comment.objects.all())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['parent'].widget.attrs.update(
            {'class': 'd-none'})
        self.fields['parent'].label = ''
        self.fields['parent'].required = False
        self.fields['name'].label = ''
        self.fields['email'].label = ''
        self.fields['content'].label = ''


    class Meta:
        model = Comment
        fields = ('name', 'parent', 'email', 'content')

        widgets = {
            'name': forms.TextInput(attrs={'class':'comment_input comment_input_name','placeholder':' Your Name', 'required':'required'}),
            'email': forms.EmailInput(attrs={'class': 'comment_input comment_input_email','placeholder':' Your Email', 'required':'required'}),
            'content': forms.Textarea(attrs={'class': 'comment_text','placeholder':' Your Comment', 'required':'required'}),
        }

    def save(self, *args, **kwargs):
        Comment.objects.rebuild()
        return super(NewCommentForm, self).save(*args, **kwargs)



class PostSearchForm(forms.Form):
    q = forms.CharField()
    c = forms.ModelChoiceField(
        queryset=Category.objects.all().order_by('title'))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['c'].label = ''
        self.fields['c'].required = False
        self.fields['c'].label = 'Category'
        self.fields['q'].label = 'Search For'
        self.fields['q'].widget.attrs.update(
            {'class': 'form-control'})
