from django.db import models
from django.utils import timezone

class AdmissionApplication(models.Model):
    # Student Information
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    applying_for_grade = models.CharField(max_length=10)
    
    # Parent/Guardian Information
    parent_first_name = models.CharField(max_length=100)
    parent_last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    
    # Application Details
    previous_school = models.CharField(max_length=200, blank=True, null=True)
    additional_information = models.TextField(blank=True, null=True)
    documents = models.FileField(upload_to='admission_documents/', blank=True, null=True)
    
    # Application Status
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('reviewing', 'Under Review'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    
    # Timestamps
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} - Grade {self.applying_for_grade}"
    
    class Meta:
        ordering = ['-created_at']
