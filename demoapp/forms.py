from django import forms


class AuthForm(forms.Form):
    signs = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'signs'}))
