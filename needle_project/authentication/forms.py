from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from authentication.models import UserProfile
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=50,)

    class Meta:
        model = User
        fields = ['first_name','last_name', 'username', 'email', 'password1', 'password2']

class UserSettingsForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']

class UserProfileForm(forms.ModelForm):
    current_password = forms.CharField(widget=forms.PasswordInput, label='Enter the current Password to change the following data', )
    class Meta:
        model=UserProfile
        fields=['image', 'background_cover','current_password','intro', 'contact_number']

class CustomPasswordResetForm(PasswordResetForm):
        def clean_email(self):
            email = self.cleaned_data['email']
            User = get_user_model()
            if not User.objects.filter(email=email).exists():
                raise ValidationError('The email address does not exist in our system.')
            return email
