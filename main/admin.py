from django.contrib import admin
from django.utils.html import format_html
from .models import Page, AboutPage, AcademicsPage, CurriculumPage, StudentLifePage, ContactPage, FAQ

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_published', 'created_at', 'updated_at')
    list_filter = ('is_published', 'created_at')
    search_fields = ('title', 'content', 'meta_description')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('created_at', 'updated_at')

@admin.register(AboutPage)
class AboutPageAdmin(admin.ModelAdmin):
    list_display = ('page', 'get_page_status', 'created_at')
    list_filter = ('page__is_published',)
    search_fields = ('page__title', 'mission_statement', 'vision_statement')
    readonly_fields = ('created_at', 'updated_at')

    def get_page_status(self, obj):
        return format_html(
            '<span style="color: {};">{}</span>',
            'green' if obj.page.is_published else 'red',
            'Published' if obj.page.is_published else 'Draft'
        )
    get_page_status.short_description = 'Status'

@admin.register(AcademicsPage)
class AcademicsPageAdmin(admin.ModelAdmin):
    list_display = ('page', 'get_page_status', 'created_at')
    list_filter = ('page__is_published',)
    search_fields = ('page__title', 'programs_overview', 'curriculum_overview')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Page Reference', {
            'fields': ('page',)
        }),
        ('Programs', {
            'fields': ('programs_overview', 'curriculum_overview')
        }),
        ('Faculty', {
            'fields': ('faculty_highlight', 'academic_support')
        }),
        ('Media', {
            'fields': ('featured_image',)
        })
    )

    def get_page_status(self, obj):
        return format_html(
            '<span style="color: {};">{}</span>',
            'green' if obj.page.is_published else 'red',
            'Published' if obj.page.is_published else 'Draft'
        )
    get_page_status.short_description = 'Status'

@admin.register(CurriculumPage)
class CurriculumPageAdmin(admin.ModelAdmin):
    list_display = ('page', 'grade_level', 'get_page_status', 'created_at')
    list_filter = ('grade_level', 'page__is_published')
    search_fields = ('page__title', 'grade_level', 'subjects')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Page Reference', {
            'fields': ('page',)
        }),
        ('Grade Information', {
            'fields': ('grade_level',)
        }),
        ('Curriculum Details', {
            'fields': ('subjects', 'learning_outcomes')
        }),
        ('Media', {
            'fields': ('featured_image',)
        })
    )

    def get_page_status(self, obj):
        return format_html(
            '<span style="color: {};">{}</span>',
            'green' if obj.page.is_published else 'red',
            'Published' if obj.page.is_published else 'Draft'
        )
    get_page_status.short_description = 'Status'

@admin.register(StudentLifePage)
class StudentLifePageAdmin(admin.ModelAdmin):
    list_display = ('page', 'get_page_status', 'created_at')
    list_filter = ('page__is_published',)
    search_fields = ('page__title', 'activities', 'clubs')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Page Reference', {
            'fields': ('page',)
        }),
        ('Activities', {
            'fields': ('activities',)
        }),
        ('Clubs and Sports', {
            'fields': ('clubs', 'sports')
        }),
        ('Media', {
            'fields': ('featured_image',)
        })
    )

    def get_page_status(self, obj):
        return format_html(
            '<span style="color: {};">{}</span>',
            'green' if obj.page.is_published else 'red',
            'Published' if obj.page.is_published else 'Draft'
        )
    get_page_status.short_description = 'Status'

@admin.register(ContactPage)
class ContactPageAdmin(admin.ModelAdmin):
    list_display = ('page', 'email', 'phone', 'get_page_status', 'created_at')
    list_filter = ('page__is_published',)
    search_fields = ('page__title', 'address', 'email', 'phone')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Page Reference', {
            'fields': ('page',)
        }),
        ('Contact Information', {
            'fields': ('address', 'phone', 'email', 'office_hours')
        }),
        ('Map', {
            'fields': ('map_embed_code',)
        }),
        ('Media', {
            'fields': ('featured_image',)
        })
    )

    def get_page_status(self, obj):
        return format_html(
            '<span style="color: {};">{}</span>',
            'green' if obj.page.is_published else 'red',
            'Published' if obj.page.is_published else 'Draft'
        )
    get_page_status.short_description = 'Status'

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'category', 'is_published', 'order', 'created_at')
    list_filter = ('category', 'is_published')
    search_fields = ('question', 'answer', 'category')
    list_editable = ('order', 'is_published')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Question', {
            'fields': ('question', 'answer')
        }),
        ('Organization', {
            'fields': ('category', 'order')
        }),
        ('Status', {
            'fields': ('is_published',)
        })
    )
