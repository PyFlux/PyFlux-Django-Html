from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _



def validate_domainonly_email(value):
    if not "gmail.com" in value:
        raise ValidationError("All emails have to be registered on :@gmail.com only.")
