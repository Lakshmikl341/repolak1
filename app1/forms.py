from django import forms
from .models import RegistersModel
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
class LoginForm(forms.ModelForm):
    class Meta:
        model=RegistersModel
        fields='__all__'
        widgets={'password':forms.PasswordInput}
#
# class CustomCreationForm(UserCreationForm):
#     class Meta:
#         model= RegistersModel
#         fields=('email','password')
# class CustomUserChangeForm(UserChangeForm):
#     class Meta:
#         model=RegistersModel
#         fields=UserChangeForm.Meta.fields
