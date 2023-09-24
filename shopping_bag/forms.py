from django import forms


class BuyCryptoForm(forms.Form):
    crypto_id = forms.CharField(widget=forms.HiddenInput())
    amount = forms.DecimalField(label='Amount')


class SellCryptoForm(forms.Form):
    crypto_id = forms.CharField(widget=forms.HiddenInput())
    amount = forms.DecimalField(label='Amount')
