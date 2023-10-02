from django import forms
from django.core.exceptions import ValidationError


class AddToBagForm(forms.Form):
    """ Add to bag form"""
    crypto_id = forms.CharField(widget=forms.HiddenInput())
    amount = forms.DecimalField(label='Amount')

    def clean_amount(self):
        """ Check if the amount is greater thean 0"""
        amount = self.cleaned_data.get('amount')
        if amount <= 0:
            raise ValidationError("Amount must be greater than zero.")
        return amount


class RemoveFromBagForm(forms.Form):
    """ Remove from bag form"""
    crypto_id = forms.CharField(widget=forms.HiddenInput())
    amount = forms.DecimalField(label='Amount')

    def clean_amount(self):
        """ Check if the amount is greater thean 0"""
        amount = self.cleaned_data.get('amount')
        if amount <= 0:
            raise ValidationError("Amount must be greater than zero.")
        return amount
