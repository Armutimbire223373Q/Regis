from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AdmissionApplicationForm

# Create your views here.

def index(request):
    return render(request, 'admissions/index.html')

def apply(request):
    if request.method == 'POST':
        form = AdmissionApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save()
            messages.success(request, 'Your application has been submitted successfully. We will contact you soon.')
            return redirect('admissions:apply')
        else:
            messages.error(request, 'There was an error with your submission. Please correct the errors below.')
    else:
        form = AdmissionApplicationForm()
    
    return render(request, 'admissions/apply.html', {'form': form})
