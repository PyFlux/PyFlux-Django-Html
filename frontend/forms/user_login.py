from django import forms
from django.core.validators import RegexValidator
from frontend.validators import common_validators


class userLogin(forms.Form):
    username = forms.CharField(label='User Name', required="required", disabled="", min_length=6, max_length=128,
                               help_text="",
                               widget=forms.TextInput(
                                   attrs={
                                       'style': '',
                                       'placeholder': '',
                                   }
                               ))
    first_name = forms.CharField(label='First Name', required="required", disabled="", min_length=6, max_length=128,
                                 help_text="")
    last_name = forms.CharField(label='Last Name', required="required", disabled="", min_length=6, max_length=128,
                                help_text="")
    email = forms.EmailField(label='Email', required="required", disabled="", min_length=6, max_length=128,
                             help_text="")

    password = forms.CharField(label='Password', required="required", disabled="", min_length=6, max_length=128,
                               help_text="", validators=[
            RegexValidator('^(\w+\d+|\d+\w+)+$', message="Password should be a combination of Alphabets and Numbers")])
    confirm_password = forms.CharField(label='Confirm Password', required="required", disabled="", min_length=6,
                                       max_length=128,
                                       help_text="")

    def clean(self):
        cleaned_data = super(userLogin, self).clean()
        username = cleaned_data.get('username')
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if not username and not first_name and not last_name and not email and not password and not confirm_password:
            raise forms.ValidationError('There are errors in the fields...!')
