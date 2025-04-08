from django.db import models
from django.utils.text import slugify
from django.core.validators import MinLengthValidator
from django.utils.translation import gettext_lazy as _

class Page(models.Model):
    """Base model for static pages."""
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    meta_description = models.CharField(max_length=160, blank=True)
    featured_image = models.ImageField(upload_to='pages/', blank=True, null=True)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = _('Page')
        verbose_name_plural = _('Pages')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class AboutPage(models.Model):
    """Model for the About page content."""
    page = models.OneToOneField(Page, on_delete=models.CASCADE, related_name='about_page')
    mission_statement = models.TextField()
    vision_statement = models.TextField()
    values = models.TextField()
    history = models.TextField()
    leadership_team = models.TextField(help_text="HTML content for leadership team section")
    featured_image = models.ImageField(upload_to='about/', blank=True, null=True)

    class Meta:
        verbose_name = _('About Page')
        verbose_name_plural = _('About Pages')

    def __str__(self):
        return f"About Page - {self.page.title}"

class AcademicsPage(models.Model):
    """Model for the Academics page content."""
    page = models.OneToOneField(Page, on_delete=models.CASCADE, related_name='academics_page')
    programs_overview = models.TextField()
    curriculum_overview = models.TextField()
    faculty_highlight = models.TextField()
    academic_support = models.TextField()
    featured_image = models.ImageField(upload_to='academics/', blank=True, null=True)

    class Meta:
        verbose_name = _('Academics Page')
        verbose_name_plural = _('Academics Pages')

    def __str__(self):
        return f"Academics Page - {self.page.title}"

class CurriculumPage(models.Model):
    """Model for the Curriculum page content."""
    page = models.OneToOneField(Page, on_delete=models.CASCADE, related_name='curriculum_page')
    grade_level = models.CharField(max_length=50)
    subjects = models.TextField()
    learning_outcomes = models.TextField()
    featured_image = models.ImageField(upload_to='curriculum/', blank=True, null=True)

    class Meta:
        verbose_name = _('Curriculum Page')
        verbose_name_plural = _('Curriculum Pages')

    def __str__(self):
        return f"{self.page.title} - {self.grade_level}"

class StudentLifePage(models.Model):
    """Model for the Student Life page content."""
    page = models.OneToOneField(Page, on_delete=models.CASCADE, related_name='student_life_page')
    activities = models.TextField()
    clubs = models.TextField()
    sports = models.TextField()
    featured_image = models.ImageField(upload_to='student_life/', blank=True, null=True)

    class Meta:
        verbose_name = _('Student Life Page')
        verbose_name_plural = _('Student Life Pages')

    def __str__(self):
        return f"Student Life Page - {self.page.title}"

class ContactPage(models.Model):
    """Model for the Contact page content."""
    page = models.OneToOneField(Page, on_delete=models.CASCADE, related_name='contact_page')
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    office_hours = models.TextField()
    map_embed_code = models.TextField(blank=True, help_text="Google Maps embed code")
    featured_image = models.ImageField(upload_to='contact/', blank=True, null=True)

    class Meta:
        verbose_name = _('Contact Page')
        verbose_name_plural = _('Contact Pages')

    def __str__(self):
        return f"Contact Page - {self.page.title}"

class FAQ(models.Model):
    """Model for Frequently Asked Questions."""
    question = models.CharField(max_length=200)
    answer = models.TextField()
    category = models.CharField(max_length=50)
    is_published = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'created_at']
        verbose_name = _('FAQ')
        verbose_name_plural = _('FAQs')

    def __str__(self):
        return self.question
