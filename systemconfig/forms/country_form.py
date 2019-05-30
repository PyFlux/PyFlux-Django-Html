from django import forms


class CountryForm(forms.Form):
    country_name = forms.CharField(label='Country', required="required", max_length=254)
    status = forms.ChoiceField(label='Status', required="required", choices=((1, 'Publish'), (2, 'Unpublish')))
