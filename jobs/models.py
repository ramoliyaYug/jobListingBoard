from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils import timezone


class Job(models.Model):
    JOB_TYPE_CHOICES = [
        ('FT', 'Full Time'),
        ('PT', 'Part Time'),
        ('INTERN', 'Internship'),
    ]

    STATUS_CHOICES = [
        ('DRAFT', 'Draft'),
        ('PUBLISHED', 'Published'),
        ('ARCHIVED', 'Archived'),
    ]

    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    job_type = models.CharField(max_length=10, choices=JOB_TYPE_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='DRAFT')
    posted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-posted_at']
        indexes = [
            models.Index(fields=['status', 'job_type']),
        ]

    def __str__(self):
        return f"{self.title} at {self.company}"


class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    name = models.CharField(max_length=200)
    email = models.EmailField()
    cover_letter = models.TextField(blank=True, null=True)
    resume = models.FileField(
        upload_to='resumes/',
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx'])]
    )
    applied_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-applied_at']
        unique_together = ('job', 'email')  # Prevent duplicate applications

    def __str__(self):
        return f"{self.name} - {self.job.title}"
