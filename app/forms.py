from django import forms
from django.forms.fields import IntegerField
from .models import PurchaseModel

class PurchaseForm(forms.ModelForm):
    
    class Meta:

        model = PurchaseModel
        fields = ('name','qty','total_amt')
        widgets = {
            'qty':forms.HiddenInput(),
        }
       