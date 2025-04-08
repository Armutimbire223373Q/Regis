from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, UpdateView, TemplateView

from .forms import (
    CustomUserCreationForm, CustomUserChangeForm,
    UserProfileForm, EmailVerificationForm
)
from .models import CustomUser


class SignUpView(CreateView):
    """View for user registration."""
    
    form_class = CustomUserCreationForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('accounts:email_verification')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        messages.success(self.request, _('Account created successfully!'))
        return response


class CustomLoginView(LoginView):
    """Custom login view."""
    
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('accounts:profile')

    def form_invalid(self, form):
        messages.error(self.request, _('Invalid email or password.'))
        return super().form_invalid(form)


@method_decorator(login_required, name='dispatch')
class ProfileView(UpdateView):
    """View for user profile management."""
    
    model = CustomUser
    form_class = UserProfileForm
    template_name = 'accounts/profile.html'
    success_url = reverse_lazy('accounts:profile')

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, _('Profile updated successfully!'))
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class EmailVerificationView(TemplateView):
    """View for email verification."""
    
    template_name = 'accounts/email_verification.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = EmailVerificationForm()
        return context

    def post(self, request, *args, **kwargs):
        form = EmailVerificationForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            # Add verification logic here
            user = request.user
            user.is_email_verified = True
            user.save()
            messages.success(request, _('Email verified successfully!'))
            return redirect('accounts:profile')
        return self.render_to_response({'form': form})


@login_required
def logout_view(request):
    """View for user logout."""
    logout(request)
    messages.info(request, _('You have been logged out.'))
    return redirect('accounts:login')
