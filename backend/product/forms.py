from django import forms

from .models import Product

class ProductForm(forms.ModelFrom):
    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
        ]