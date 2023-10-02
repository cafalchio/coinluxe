from django import forms
from .models import CryptoCurrency


class CryptoCurrencyForm(forms.ModelForm):
    """Crypto Form """
    class Meta:
        """ Meta """
        model = CryptoCurrency
        fields = "__all__"


class CryptoCurrencyEditForm(forms.ModelForm):
    """Crypto Edit Form """
    class Meta:
        """ Meta """
        model = CryptoCurrency
        fields = "__all__"
