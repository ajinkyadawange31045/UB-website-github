from django import forms

from .models import Comment, Topic

class CreateTopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = [
            'title', 'description'
        ]

class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        widgets = {
            'body': forms.Textarea(attrs={'class':'comment_input_name form-control md-textarea','placeholder':' Add your opinion here', 'required':'required'}),
           
        }
        fields = [
            'body', 'author', 'post'
        ]