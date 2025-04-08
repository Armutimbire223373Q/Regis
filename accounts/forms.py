from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import gettext_lazy as _

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """Form for creating new users."""
    
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'user_type', 
                 'date_of_birth', 'phone_number')
        
    def clean_email(self):
        """Validate email is unique."""
        email = self.cleaned_data['email']
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError(_('This email is already registered.'))
        return email


class CustomUserChangeForm(UserChangeForm):
    """Form for updating users."""
    
    password = None  # Remove password field from the form
    
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'date_of_birth',
                 'phone_number', 'address', 'bio', 'profile_picture')
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }


class UserProfileForm(forms.ModelForm):
    """Form for users to update their profile."""
    
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'phone_number', 'address',
                 'bio', 'profile_picture')
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4}),
        }


class EmailVerificationForm(forms.Form):
    """Form for email verification code."""
    
    code = forms.CharField(
        label=_('Verification Code'),
        max_length=6,
        min_length=6,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': _('Enter 6-digit code')
        })
    )
