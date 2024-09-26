from django import forms
from .models import Resume, JobDescription

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['user_name', 'file']

class JobDescriptionForm(forms.ModelForm):
    class Meta:
        model = JobDescription
        fields = ['title', 'description']
