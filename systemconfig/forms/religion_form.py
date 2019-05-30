from django import forms


class ReligionForm(forms.Form):
    student_religion = forms.CharField(label='Religion', required="required", max_length=254)
    status = forms.ChoiceField(label='Status', required="required",choices=((1, 'Publish'), (2, 'Unpublish')))
