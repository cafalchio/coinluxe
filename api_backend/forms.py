from django import forms
from .models import CryptoCurrency


class CryptoCurrencyForm(forms.ModelForm):
    class Meta:
        model = CryptoCurrency
        fields = "__all__"


class CryptoCurrencyEditForm(forms.ModelForm):
    class Meta:
        model = CryptoCurrency
        fields = "__all__"
