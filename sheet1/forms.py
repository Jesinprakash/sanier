from django import forms

from sheet1.models import Sheet


from django import forms
from .models import Sheet

class SheetForm(forms.ModelForm):
    class Meta:
        model = Sheet
        fields = ["name", "dob"]
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter full name"
            }),
            "dob": forms.DateInput(attrs={
                "class": "form-control",
                "type": "date"
            }),
        }



