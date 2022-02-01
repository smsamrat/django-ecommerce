from dataclasses import field
from django import forms
from payment.models import BillingAddress

class BillingAddressForm(forms.ModelForm):
    class Meta:
        model = BillingAddress
        fields = ['first_name','last_name','address1','address2','country','zip','city','phone']