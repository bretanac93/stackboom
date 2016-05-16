from django.contrib.auth.models import User
from django.forms import ModelForm, CharField, PasswordInput
from django.utils.translation import ugettext, ugettext_lazy as _

class RegistrationForm(ModelForm):

    password1 = CharField(widget=PasswordInput)
    password2 = CharField(widget=PasswordInput, help_text="Enter the same password as before, for verification.")

    class Meta:
        model = User
        fields = ("username","email", "first_name", "last_name",)