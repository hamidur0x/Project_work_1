from django import forms
from .models import Sale


class SaleForm(forms.ModelForm):

    class Meta:
        model = Sale
        fields = [
            "product",
            "quantity"
        ]

        widgets = {
            "quantity": forms.NumberInput(
                attrs={
                    "min": 1
                }
            )
        }