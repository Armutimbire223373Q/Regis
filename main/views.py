from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from blog.models import Post
from .models import (
    AboutPage, AcademicsPage, CurriculumPage,
    StudentLifePage, ContactPage, FAQ
)
from .forms import ContactForm

# Create your views here.

def home(request):
    """Home page view."""
    latest_posts = Post.objects.filter(status='published').order_by('-created')[:3]
    return render(request, 'main/home.html', {'latest_posts': latest_posts})

def about(request):
    """About page view."""
    about_page = get_object_or_404(AboutPage, is_published=True)
    return render(request, 'main/about.html', {'about_page': about_page})

def academics(request):
    """Academics page view."""
    academics_page = get_object_or_404(AcademicsPage, is_published=True)
    return render(request, 'main/academics.html', {'academics_page': academics_page})

def curriculum(request):
    """Curriculum page view."""
    curriculum_pages = CurriculumPage.objects.filter(is_published=True).order_by('grade_level')
    return render(request, 'main/curriculum.html', {'curriculum_pages': curriculum_pages})

def student_life(request):
    """Student Life page view."""
    student_life_page = get_object_or_404(StudentLifePage, is_published=True)
    return render(request, 'main/student_life.html', {'student_life_page': student_life_page})

def news(request):
    """News page view - redirects to blog."""
    return render(request, 'main/news.html')

def parents(request):
    """Parents page view."""
    faqs = FAQ.objects.filter(is_published=True).order_by('order')
    return render(request, 'main/parents.html', {'faqs': faqs})

def contact(request):
    """Contact page view."""
    contact_page = get_object_or_404(ContactPage, is_published=True)
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                form.send_email()
                messages.success(request, 'Your message has been sent successfully!')
                return redirect('main:contact')
            except Exception as e:
                messages.error(request, 'There was an error sending your message. Please try again later.')
    else:
        form = ContactForm()
    
    return render(request, 'main/contact.html', {
        'contact_page': contact_page,
        'form': form
    })
