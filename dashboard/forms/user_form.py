from django import forms
from django.core.validators import RegexValidator
from dashboard.validators import validate_domainonly_email


class addUserForm(forms.Form):
    username = forms.CharField(label='User Name', required="required", disabled="", min_length=6, max_length=128,
                               help_text="",
                               widget=forms.TextInput(
                                   attrs={
                                       'style': '',
                                       'placeholder': '',
                                   }
                               ))
    first_name = forms.CharField(label='First Name', required="required", disabled="", min_length=3, max_length=128,
                                 help_text="")
    last_name = forms.CharField(label='Last Name', required="required", disabled="", min_length=3, max_length=128,
                                help_text="")
    email = forms.EmailField(label='Email', required="required", disabled="", min_length=6, max_length=128,
                             help_text="", validators=[validate_domainonly_email])

    password = forms.CharField(label='Password', required="required", disabled="", min_length=6, max_length=128,
                               help_text="", validators=[
            RegexValidator('^(\w+\d+|\d+\w+)+$', message="Password should be a combination of Alphabets and Numbers")])
    confirm_password = forms.CharField(label='Confirm Password', required="required", disabled="", min_length=6,
                                       max_length=128,
                                       help_text="")

    def clean(self):
        cleaned_data = super(addUserForm, self).clean()
        username = cleaned_data.get('username')
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if not username and not first_name and not last_name and not email and not password and not confirm_password:
            raise forms.ValidationError('There are errors in the fields...!')

# class editUserForm(forms.Form):
#     username = forms.CharField(label='User Name', required="required", disabled="disabled", min_length="6",
#                                max_length=128, help_text="")
#     first_name = forms.CharField(label='First Name', max_length=254, help_text="")
#     last_name = forms.CharField(label='Last Name', max_length=254, help_text="")
#     email = forms.EmailField(label='Email', max_length=8, help_text="")
#
#     def clean(self):
#         cleaned_data = super(editUserForm, self).clean()
#         username = cleaned_data.get('username')
#         first_name = cleaned_data.get('first_name')
#         last_name = cleaned_data.get('last_name')
#         email = cleaned_data.get('email')
#         if not username and not first_name and not last_name and not email:
#             raise forms.ValidationError('There are errors in the fields...!')
