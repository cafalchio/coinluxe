from django import forms
from .models import CryptoCurrency

class CryptoCurrencyForm(forms.ModelForm):
    class Meta:
        model = CryptoCurrency
        fields = ['id', 'sell_price_multiplier']