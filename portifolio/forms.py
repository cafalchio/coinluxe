from django import forms


class AddCreditsForm(forms.Form):
    product_price = forms.DecimalField(label='Product Price')