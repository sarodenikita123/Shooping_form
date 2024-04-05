from django import forms
from .models import Shopping


class ShoppingForm(forms.ModelForm):
    class Meta:
        model = Shopping
        fields = "__all__"

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "address": forms.TextInput(attrs={"class": "form-control"}),
            "phone": forms.NumberInput(),
            "email": forms.TextInput(attrs={"class": "form-control"}),
            "quantity": forms.RadioSelect(),
            "destination": forms.TextInput(attrs={"class": "form-control"}),
            "arrival_date": forms.DateInput(attrs={"type": "date"}),
            "return_date": forms.DateInput(attrs={"type": "date"})
        }
