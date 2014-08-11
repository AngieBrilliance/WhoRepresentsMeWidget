from django import forms

class EnterAddressForm(forms.Form):
	address = forms.CharField(label="address", max_length=255, required=True)
