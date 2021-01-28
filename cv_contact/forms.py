from django import forms


class ContactUs(forms.Form):
    full_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': "form-control", 'placeholder': "Full Name"}))

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': "form-control", 'placeholder': "email"}))

    massage = forms.CharField(widget=forms.Textarea(
        attrs={'class': "form-control", 'placeholder': "massage"}))
