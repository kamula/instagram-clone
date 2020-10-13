from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import useraccount

class registrationform(UserCreationForm):
    email = forms.EmailField(max_length=30)

    class Meta:
        model = useraccount
        fields = ('email','fullname','username','phone_number')


class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='password',widget=forms.PasswordInput)
    class Meta:
        model = useraccount
        fields = ('email','password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email = email,password = password):
                raise forms.ValidationError('invalid login credentials')
