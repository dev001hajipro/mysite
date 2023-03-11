from django import forms
from .models import Contact


# https://stackoverflow.com/questions/50214773/type-datetime-local-in-django-form
class DateTimeLocalInput(forms.DateTimeInput):
    input_type = "datetime-local"


class DateTimeLocalField(forms.DateTimeField):
    # Set DATETIME_INPUT_FORMATS here because, if USE_L10N
    # is True, the locale-dictated format will be applied
    # instead of settings.DATETIME_INPUT_FORMATS.
    # See also:
    # https://developer.mozilla.org/en-US/docs/Web/HTML/Date_and_time_formats

    input_formats = [
        "%Y-%m-%dT%H:%M:%S",
        "%Y-%m-%dT%H:%M:%S.%f",
        "%Y-%m-%dT%H:%M"
    ]
    widget = DateTimeLocalInput(format="%Y-%m-%dT%H:%M")


class ConcatForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
    # input type="datetime-local"に対応
    pub_date = DateTimeLocalField()

@DeprecationWarning
class ContactSearchListForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
    
    pub_date = DateTimeLocalField()
