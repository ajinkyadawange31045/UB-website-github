from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,UserChangeForm
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from .models import Profile


# from mptt.forms import TreeNodeChoiceField
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label='', max_length=30, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'First Name', 'style': 'font-weight: bold; font-weight: bold;'}), help_text='<small class="text-muted">Optional</small>', )
    last_name = forms.CharField(label='', max_length=30, required=False, widget=forms.TextInput(attrs={'class': 'form-control','placeholder' : 'Last Name', 'style': 'font-weight: bold;'}), help_text='<small class="text-muted">Optional</small>')
    email = forms.EmailField(label='', max_length=254, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder' : 'Email-Id'}), help_text='<small class="text-muted">Enter a valid email address</small>')

    # profile_image = forms.ImageField(required=True, widget=forms.FileInput(attrs={'class': 'form-control'}), help_text='<small class="text-danger">Upload a profile picture of less than 2mb</small>')
    password1 = forms.CharField(label='',widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder' : 'Password'}))
    password2 = forms.CharField(label='',widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder' : 'Confirm Password(again)'}))

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        # fields = ['username','first_name','last_name','email', 'profile_image']
        labels = {'username' : '', 'first_name':'<strong>First Name</strong>','last_name':'<strong>Last Name</strong>','email':'<strong>Email</strong>', 'profile_image': '<strong>Profile Image</strong>'}

        widgets = {'username':forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'Username'}),
        'first_name':forms.TextInput(attrs={'class':'form-control', 'style': 'font-weight: bold;'}),
        'last_name':forms.TextInput(attrs={'class':'form-control', 'style': 'font-weight: bold;'}),
        'email':forms.EmailInput(attrs={'class':'form-control'}),
        }


# class SignUpForm(UserCreationForm):
#     first_name = forms.CharField(max_length=30, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'color: black; font-weight: bold;'}), help_text='Optional')
#     last_name = forms.CharField(max_length=30, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'font-weight: bold;'}), help_text='Optional')
#     email = forms.EmailField(max_length=254, widget=forms.EmailInput(attrs={'class': 'form-control'}), help_text='Enter a valid email address')

#     password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
#     password2 = forms.CharField(label='Confirm Password(again)',widget=forms.PasswordInput(attrs={'class':'form-control'}))

#     # Add the profile image field here
#     profile_image = forms.ImageField(required=True)

#     class Meta:
#         model = User
#         fields = ['username','first_name','last_name','email', 'profile_image']
#         labels = {'first_name':'<strong>First Name</strong>','last_name':'<strong>Last Name</strong>','email':'<strong>Email</strong>'}

#         widgets = {'username':forms.TextInput(attrs={'class':'form-control'}),
#         'first_name':forms.TextInput(attrs={'class':'form-control', 'style': 'font-weight: bold;'}),
#         'last_name':forms.TextInput(attrs={'class':'form-control', 'style': 'font-weight: bold;'}),
#         'email':forms.EmailInput(attrs={  'type':"email",'id':"form3Example3@nitk.edu.in",'class':'form-control'}),
#         }



class LoginForm(AuthenticationForm):
    # <input type="email" id="typeEmailX-2" class="form-control form-control-lg" />
   username = UsernameField(widget=forms.EmailInput(attrs={'type':"email" ,'id':'typeEmailX-2' ,'class':"form-control form-control-lg mb-2"}))#we are doing it simply because we need to write the bootstrap class
#    username = UsernameField(widget=forms.EmailInput(attrs={'autofocus':True,'class':'form-control'}))#we are doing it simply because we need to write the bootstrap class
   password = forms.CharField(
    label = _("Password "),
    strip=False, 
    widget = forms.PasswordInput(attrs={
        'autocomplete':'current-password',
        'class':"form-control form-control-lg mb-2"
        })
    )

# Edit user
# class EditUserProfileForm(UserChangeForm):
#     password = None
#     # last_login = None
#     class Meta:
#         model = User
#         fields = ['username','first_name','last_name'] 
#         lables = {'email':'Email'}


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username', 
            'first_name', 
            'last_name', 
            'email', 
        ]

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'location', 'birth_date','phone_number','website','github','twitter','instagram','facebook', 'profile_image')
        widgets = {
            'profile_image': forms.FileInput(attrs={'accept': 'image/*','placeholder': 'optional'}),
            'bio': forms.Textarea(attrs={'rows': 3,'placeholder': 'optional'}),
            'location': forms.TextInput(attrs={'placeholder': 'City, State, Country'}),
            'website': forms.TextInput(attrs={'placeholder': 'optional (put https links )'}),
            'github': forms.TextInput(attrs={'placeholder': 'optional (put https links )'}),
            'instagram': forms.TextInput(attrs={'placeholder': 'optional (put https links )'}),
            'twitter': forms.TextInput(attrs={'placeholder': 'optional (put https links )'}),
            'facebook': forms.TextInput(attrs={'placeholder': 'optional (put https links )'}),
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['profile_image'].widget.clear_checkbox_label = ''
