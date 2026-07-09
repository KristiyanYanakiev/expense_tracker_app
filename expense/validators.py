from xml.dom import ValidationErr

from django.core.exceptions import ValidationError


def positive_float_validators(value):
    if value <= 0.0:
        raise ValidationError('The expense should be positive float number')