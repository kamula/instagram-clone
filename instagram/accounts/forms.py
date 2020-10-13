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

class Accountupdateform(forms.ModelForm):
    class Meta:
        model=useraccount
        fields = ('email','username')
    def clean_mail(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            try:
                account = useraccount.objects.exclude(pk=self.instance.pk).get(email=email)
            except useraccount.DoesNotExist:
                return email
        raise forms.ValidationError('Email "%s" is already in use.'% email)

    def clean_username(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            try:
                account = useraccount.objects.exclude(pk=self.instance.pk).get(username=username)
            except useraccount.DoesNotExist:
                return username
        raise forms.ValidationError('username "%s" is already in use.'% username)
