from django import forms


class RelationshipForm(forms.Form):
    name = forms.CharField(label='Relationship', required="required", max_length=254)
    status = forms.ChoiceField(label='Status', required="required", choices=((1, 'Publish'), (2, 'Unpublish')))
