from django import forms
from django.core.validators import RegexValidator
from frontend.validators import common_validators


class userRegister(forms.Form):
    username = forms.CharField(label='User Name', required="required", disabled="", min_length=6, max_length=128,
                               help_text="",
                               widget=forms.TextInput(
                                   attrs={
                                       'style': '',
                                       'placeholder': 'Eg: john123',
                                       'class': 'form-control',
                                   }
                               ))
    full_name = forms.CharField(label='Your Name', required="required", disabled="", min_length=6, max_length=128,
                                 help_text="", widget=forms.TextInput(
            attrs={
                'style': '',
                'placeholder': 'Eg: John Doe',
                'class': 'form-control',
            }
        ))

    email = forms.EmailField(label='Email', required="required", disabled="", min_length=6, max_length=128,
                             help_text="", widget=forms.TextInput(
            attrs={
                'style': '',
                'placeholder': 'Email',
                'class': 'form-control',
            }
        ))

    password = forms.CharField(label='Password', required="required", disabled="", min_length=6, max_length=128,
                               help_text="", widget=forms.PasswordInput(
            attrs={
                'style': '',
                'placeholder': 'Password',
                'class': 'form-control',
            }
        ), validators=[
            RegexValidator('^(\w+\d+|\d+\w+)+$', message="Password should be a combination of Alphabets and Numbers")])
    confirm_password = forms.CharField(label='Confirm Password', required="required", disabled="", min_length=6,
                                       max_length=128,
                                       help_text="", widget=forms.PasswordInput(
            attrs={
                'style': '',
                'placeholder': 'Confirm Password',
                'class': 'form-control',
            }
        ))

    def clean(self):
        cleaned_data = super(userRegister, self).clean()
        username = cleaned_data.get('username')
        full_name = cleaned_data.get('full_name')
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if not username and not full_name and not email and not password and not confirm_password:
            raise forms.ValidationError('There are errors in the fields...!')
