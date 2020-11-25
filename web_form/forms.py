from django import forms
from captcha.fields import CaptchaField

from .models import Article


class ArticleForm(forms.ModelForm):
    captcha = CaptchaField(label='Докажи что не робот ')

    class Meta:
        model = Article
        fields = '__all__'
