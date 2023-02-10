from django import forms
from hello.models import LogMessage
from hello.models import userinfo

class LogMessageForm(forms.ModelForm):
    class Meta:
        model = LogMessage
        fields = ("message",)   # NOTE: the trailing comma is required

class CreateUserForm(forms.ModelForm):
    class Meta:
        model = userinfo
        fields = ("email", "phone", "gender", "firstname", "lastname", "username","password",)
        