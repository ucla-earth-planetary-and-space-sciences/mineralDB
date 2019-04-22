from django import forms
from django.core.validators import RegexValidator
from webforms.models import Webform


class Webformform(forms.ModelForm):

    class Meta:
        model = Webform
        fields = '__all__'
