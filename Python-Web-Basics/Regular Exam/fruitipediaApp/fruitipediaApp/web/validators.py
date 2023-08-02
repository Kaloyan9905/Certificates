from django.core.exceptions import ValidationError


def name_starts_with_letter_validator(value):
    if not value[0].isalpha():
        raise ValidationError('Your name must start with a letter!')


def name_consists_with_letter_only_validator(value):
    for char in value:
        if not char.isalpha():
            raise ValidationError('Fruit name should contain only letters!"')
