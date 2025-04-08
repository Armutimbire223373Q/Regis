from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import (
    LeadershipMember, TuitionFee, Scholarship, ImportantDate,
    HostelFacility, StudentService, ParentResource, PaymentMethod,
    PrivacyPolicy
)

class LeadershipTeamView(ListView):
    model = LeadershipMember
    template_name = 'school/leadership.html'
    context_object_name = 'members'
    
    def get_queryset(self):
        return LeadershipMember.objects.filter(is_active=True)

class TuitionFeesView(ListView):
    model = TuitionFee
    template_name = 'school/tuition.html'
    context_object_name = 'fees'
    
    def get_queryset(self):
        return TuitionFee.objects.filter(is_active=True)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['scholarships'] = Scholarship.objects.filter(is_active=True)
        return context

class ImportantDatesView(ListView):
    model = ImportantDate
    template_name = 'school/important_dates.html'
    context_object_name = 'dates'
    
    def get_queryset(self):
        return ImportantDate.objects.filter(is_active=True)

class StudentLifeView(ListView):
    model = HostelFacility
    template_name = 'school/student_life.html'
    context_object_name = 'facilities'
    
    def get_queryset(self):
        return HostelFacility.objects.filter(is_active=True)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = StudentService.objects.filter(is_active=True)
        return context

class ParentsCornerView(ListView):
    model = ParentResource
    template_name = 'school/parents_corner.html'
    context_object_name = 'resources'
    
    def get_queryset(self):
        return ParentResource.objects.filter(is_active=True)

class PaymentView(ListView):
    model = PaymentMethod
    template_name = 'school/payment.html'
    context_object_name = 'methods'
    
    def get_queryset(self):
        return PaymentMethod.objects.filter(is_active=True)

class PrivacyPolicyView(DetailView):
    model = PrivacyPolicy
    template_name = 'school/privacy_policy.html'
    
    def get_object(self):
        return PrivacyPolicy.objects.first()

class StudentPortalView(LoginRequiredMixin, TemplateView):
    template_name = 'school/student_portal.html'
    login_url = '/login/'

class ParentPortalView(LoginRequiredMixin, TemplateView):
    template_name = 'school/parent_portal.html'
    login_url = '/login/'

class TeacherPortalView(LoginRequiredMixin, TemplateView):
    template_name = 'school/teacher_portal.html'
    login_url = '/login/' 