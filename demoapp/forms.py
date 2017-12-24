from django import forms


# Форма авторизации
class AuthForm(forms.Form):
    signs = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'signs'}))
    user_id = forms.CharField(max_length=100, widget=forms.NumberInput(attrs={'class': 'signs'}))


# Форма регистрации
class SignInForm(forms.Form):
    userId = forms.CharField(max_length=100, widget=forms.NumberInput(attrs={'class': 'signs'}))
    # signs vectors
    signVector1 = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'signs'}))
    signVector2 = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'signs'}))
    signVector3 = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'signs'}))