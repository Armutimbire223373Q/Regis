from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django.conf import settings

class StudentProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='student_profile')
    student_id = models.CharField(max_length=20, unique=True)
    grade = models.CharField(max_length=10)
    section = models.CharField(max_length=5)
    date_of_birth = models.DateField()
    parent = models.ForeignKey('ParentProfile', on_delete=models.SET_NULL, null=True, related_name='children')

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.grade}{self.section}"

class ParentProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='parent_profile')
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    occupation = models.CharField(max_length=100)

    def __str__(self):
        return self.user.get_full_name()

class TeacherProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='teacher_profile')
    teacher_id = models.CharField(max_length=20, unique=True)
    department = models.CharField(max_length=50)
    specialization = models.CharField(max_length=100)
    joining_date = models.DateField()

    def __str__(self):
        return self.user.get_full_name()

class LeadershipMember(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    bio = models.TextField()
    photo = models.ImageField(upload_to='leadership/')
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['order', 'name']
        
    def __str__(self):
        return f"{self.name} - {self.position}"

class TuitionFee(models.Model):
    GRADE_CHOICES = [
        ('pre-school', 'Pre-School'),
        ('primary', 'Primary School'),
        ('secondary', 'Secondary School'),
        ('high', 'High School'),
    ]
    
    grade = models.CharField(max_length=20, choices=GRADE_CHOICES)
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['grade']
        
    def __str__(self):
        return f"{self.get_grade_display()} - ${self.amount}"

class Scholarship(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    requirements = models.TextField()
    deadline = models.DateField()
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['deadline']
        
    def __str__(self):
        return self.name

class ImportantDate(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['date']
        
    def __str__(self):
        return f"{self.title} - {self.date}"

class HostelFacility(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    photo = models.ImageField(upload_to='hostel/')
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return self.name

class StudentService(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=50, help_text="Font Awesome icon class")
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return self.name

class ParentResource(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    file = models.FileField(upload_to='parent_resources/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return self.title

class PaymentMethod(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    instructions = models.TextField()
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

class PrivacyPolicy(models.Model):
    content = models.TextField()
    last_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Privacy Policy - {self.last_updated}" 