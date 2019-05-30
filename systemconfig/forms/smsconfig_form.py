from django import forms


class SmsConfigForm(forms.Form):
    firm_id = forms.CharField(label='Firm', required="", max_length=254)
    sms_count = forms.CharField(label='Total Sms', required="required", max_length=254)
    api_key = forms.CharField(label='API Key', required="required", max_length=254)
    status = forms.ChoiceField(label='Status', required="required", choices=((1, 'Publish'), (2, 'Unpublish')))
