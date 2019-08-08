from django import forms
from .models import Product


class ProductCategoryList(forms.Form):

    class Meta:
        model = Product
        fields = ['category']
