from django import forms
from .models import SaleItem


class SaleItemForm(forms.ModelForm):

    class Meta:
        model = SaleItem
        fields = [
            "product",
            "quantity"
        ]