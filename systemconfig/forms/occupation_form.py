from django import forms


class OccupationForm(forms.Form):
    occupation = forms.CharField(label='Occupation', required="required", max_length=254)
    status = forms.ChoiceField(label='Status', required="required", choices=((1, 'Publish'), (2, 'Unpublish')))
