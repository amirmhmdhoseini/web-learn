from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username_or_email = forms.CharField(
        label='Username or Email',
        max_length=150
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput
    )

    def clean(self):
        cleaned_data = super().clean()

        username_or_email = cleaned_data.get('username_or_email')
        password = cleaned_data.get('password')

        if username_or_email and password:
            user = authenticate(
                username=username_or_email,
                password=password
            )

            if user is None:
                try:
                    user_obj = User.objects.get(
                        email=username_or_email
                    )

                    user = authenticate(
                        username=user_obj.username,
                        password=password
                    )

                except User.DoesNotExist:
                    user = None

            if user is None:
                raise forms.ValidationError(
                    'Username/email or password is incorrect.'
                )

            cleaned_data['user'] = user

        return cleaned_data
