from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class BuyProductForm(forms.ModelForm):
    street = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    country = forms.CharField(max_length=100)

    class Meta:
        model = Product
        exclude = ['name', 'friendly_name', 'price', 'description', 'image']

    quantity = forms.IntegerField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['quantity'].label = 'Quantity'
