from django import forms
from .models import AllCryptosList, CryptoCurrency


class AllCryptosListForm(forms.ModelForm):
    """ To add a crypto, just add the id of a real crypto and
    the management will update its fields """
    class Meta:
        """ Meta """
        model = AllCryptosList
        fields = "__all__"


class CryptoCurrencyEditForm(forms.ModelForm):
    """Crypto Edit Form """
    class Meta:
        """ Meta """
        model = CryptoCurrency
        fields = "__all__"
