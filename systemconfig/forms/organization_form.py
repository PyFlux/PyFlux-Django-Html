from django import forms
from systemconfig.validators import *


class OrganizationForm(forms.Form):
    org_name = forms.CharField(label='Name', required="required", max_length=254)
    org_alias = forms.CharField(label='Alias', required="required", max_length=254)
    org_address_line1 = forms.CharField(label='Address Line 1', required='required', max_length=255)
    org_address_line2 = forms.CharField(label='Address Line 2', required='required', max_length=255)
    org_phone = forms.CharField(label="Phone", required="required", max_length=255, validators=[validate_phone])
    org_email = forms.EmailField(label='Email Id', required="required", disabled="", min_length=6,
                                 max_length=128, help_text="", validators=[validate_email_id])
    org_website = forms.CharField(label='Website', required='required', max_length=255)
    org_logo = forms.CharField(label='Logo', required='required', max_length=255)
    org_logo_type = forms.CharField(label='Logo Type', required='required', max_length=255)
    status = forms.ChoiceField(label='Status', required="required", choices=((1, 'Publish'), (2, 'Unpublish')))
