from django import forms


class AddCreditsForm(forms.Form):
    product_price = forms.DecimalField(label='Credits')


class BuyCryptoForm(forms.Form):
    crypto_id = forms.CharField(widget=forms.HiddenInput())
    amount = forms.DecimalField(label='Amount')


class SellCryptoForm(forms.Form):
    crypto_id = forms.CharField(widget=forms.HiddenInput())
    amount = forms.DecimalField(label='Amount')
