from django.core.exceptions import ValidationError
import re
from django.core.files.images import get_image_dimensions
import os


def validate_email_id(value):
    if not "gmail.com" in value:
        raise ValidationError("All emails have to be registered on :@gmail.com only.")


def validate_phone(value):
    x = len(value)
    if not x == 10:
        raise ValidationError('phone number must be 10 digits')
    elif not bool(re.match('^[0-9]+$', value)):
        raise ValidationError('This field must not be alphabets/special characters')
    return value
