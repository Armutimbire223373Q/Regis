from django import forms
from .models import AdmissionApplication

class AdmissionApplicationForm(forms.ModelForm):
    class Meta:
        model = AdmissionApplication
        fields = [
            'first_name', 'last_name', 'date_of_birth', 'gender', 'applying_for_grade',
            'parent_first_name', 'parent_last_name', 'email', 'phone', 'address',
            'previous_school', 'additional_information', 'documents'
        ]
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'additional_information': forms.Textarea(attrs={'rows': 4}),
            'address': forms.Textarea(attrs={'rows': 3}),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
            
        # Add placeholder text
        self.fields['first_name'].widget.attrs.update({'placeholder': 'Enter first name'})
        self.fields['last_name'].widget.attrs.update({'placeholder': 'Enter last name'})
        self.fields['parent_first_name'].widget.attrs.update({'placeholder': 'Enter parent/guardian first name'})
        self.fields['parent_last_name'].widget.attrs.update({'placeholder': 'Enter parent/guardian last name'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Enter email address'})
        self.fields['phone'].widget.attrs.update({'placeholder': 'Enter phone number'})
        self.fields['previous_school'].widget.attrs.update({'placeholder': 'Enter previous school (if applicable)'})
        self.fields['additional_information'].widget.attrs.update({'placeholder': 'Any additional information you would like to share'}) 