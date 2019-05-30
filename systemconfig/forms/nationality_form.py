from django import forms


class NationalityForm(forms.Form):
    nationality_name = forms.CharField(label='Nationality', required="required", max_length=254)
    status = forms.ChoiceField(label='Status', required="required", choices=((1, 'Publish'), (2, 'Unpublish')))
