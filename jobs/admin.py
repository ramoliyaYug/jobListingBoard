from django.contrib import admin
from .models import Job, Application


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'job_type', 'status', 'posted_at')
    list_filter = ('status', 'job_type', 'posted_at')
    search_fields = ('title', 'company', 'description')
    ordering = ('-posted_at',)
    readonly_fields = ('posted_at', 'updated_at')

    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'company', 'location', 'job_type')
        }),
        ('Description', {
            'fields': ('description',)
        }),
        ('Status', {
            'fields': ('status',)
        }),
        ('Timestamps', {
            'fields': ('posted_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'job', 'applied_at')
    list_filter = ('job', 'applied_at')
    search_fields = ('name', 'email', 'job__title')
    readonly_fields = ('applied_at', 'resume_link')
    ordering = ('-applied_at',)

    fieldsets = (
        ('Applicant Information', {
            'fields': ('name', 'email')
        }),
        ('Application', {
            'fields': ('job', 'cover_letter', 'resume', 'resume_link')
        }),
        ('Timestamps', {
            'fields': ('applied_at',),
            'classes': ('collapse',)
        }),
    )

    def resume_link(self, obj):
        if obj.resume:
            return f'<a href="{obj.resume.url}" target="_blank">Download Resume</a>'
        return '-'

    resume_link.short_description = 'Resume'
    resume_link.allow_tags = True

    def has_add_permission(self, request):
        # Applications should only be created via the web form, not admin
        return False
