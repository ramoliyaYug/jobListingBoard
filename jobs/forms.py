from django import forms
from .models import Application


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['name', 'email', 'cover_letter', 'resume']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Full Name',
                'required': True,
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Email',
                'required': True,
            }),
            'cover_letter': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Optional: Tell us why you\'re interested in this role',
                'rows': 5,
            }),
            'resume': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': '.pdf,.doc,.docx',
                'required': True,
            }),
        }

    def clean_resume(self):
        resume = self.cleaned_data.get('resume')
        if resume:
            # Check file size (max 5MB)
            if resume.size > 5 * 1024 * 1024:
                raise forms.ValidationError('Resume file size must be less than 5MB.')

            # Check file extension
            allowed_extensions = ['pdf', 'doc', 'docx']
            file_extension = resume.name.split('.')[-1].lower()
            if file_extension not in allowed_extensions:
                raise forms.ValidationError('Only PDF and DOC/DOCX files are allowed.')

        return resume
