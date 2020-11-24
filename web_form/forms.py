from django import forms
from captcha.fields import CaptchaField

class Form(forms.Form):
    field = forms.CharField(label='Введите сообщение ', max_length=100)
    captcha = CaptchaField(label='Докажи что не робот ')
