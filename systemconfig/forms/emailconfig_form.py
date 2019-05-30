from django import forms


class EmailConfigForm(forms.Form):
    firm_id = forms.CharField(label='Firm', required="", max_length=254)
    per_day = forms.CharField(label='Per Day', required="required", max_length=254)
    per_month = forms.CharField(label='Per Month', required="required", max_length=254)
    status = forms.ChoiceField(label='Status', required="required", choices=((1, 'Publish'), (2, 'Unpublish')))
