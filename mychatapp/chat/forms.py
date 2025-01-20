from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'maxlength': 150}),
        }
        help_texts = {
            'username': 'Only letters and numbers are allowed.',
        }

        def clean_username(self):
            username = self.cleaned_data.get('username')
            if not username.isalnum():
                raise ValidationError("The username can only contain letters and numbers.")
            return username