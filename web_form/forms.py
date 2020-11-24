from django import forms
from captcha.fields import CaptchaField

from . import models


class InputForm(forms.ModelForm):
    captcha = CaptchaField(label='Докажи что не робот ')

    class Meta:
        model = models.Message
        fields = '__all__'
