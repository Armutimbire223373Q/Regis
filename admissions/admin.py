from django.contrib import admin
from .models import AdmissionApplication

@admin.register(AdmissionApplication)
class AdmissionApplicationAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'applying_for_grade', 'email', 'phone', 'status', 'created_at')
    list_filter = ('status', 'applying_for_grade', 'created_at')
    search_fields = ('first_name', 'last_name', 'email', 'phone')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Student Information', {
            'fields': ('first_name', 'last_name', 'date_of_birth', 'gender', 'applying_for_grade')
        }),
        ('Parent/Guardian Information', {
            'fields': ('parent_first_name', 'parent_last_name', 'email', 'phone', 'address')
        }),
        ('Application Details', {
            'fields': ('previous_school', 'additional_information', 'documents')
        }),
        ('Application Status', {
            'fields': ('status',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
