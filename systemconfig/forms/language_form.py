from django import forms


class LanguageForm(forms.Form):
    language_name = forms.CharField(label='Language', required="required", max_length=254)
    status = forms.ChoiceField(label='Status', required="required", choices=((1, 'Publish'), (2, 'Unpublish')))
