from django import forms
from django.core.mail import send_mail
from django.conf import settings

class ContactForm(forms.Form):
    """Form for contact page."""
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Your Name'
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Your Email'
        })
    )
    subject = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Subject'
        })
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Your Message',
            'rows': 5
        })
    )

    def send_email(self):
        """Send the contact form email."""
        subject = f"Contact Form: {self.cleaned_data['subject']}"
        message = f"""
        From: {self.cleaned_data['name']} ({self.cleaned_data['email']})
        
        {self.cleaned_data['message']}
        """
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [settings.CONTACT_EMAIL],
            fail_silently=False,
        ) 