from django import forms

class EnterAddressForm(forms.Form):
	address = forms.CharField(label="address", max_length=255, required=True,widget=forms.TextInput(attrs={"placeholder": "What's your address?"}))
