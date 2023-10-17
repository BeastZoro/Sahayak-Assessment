from django import forms
from .models import Students, Teachers

class CertificateForm(forms.Form):
    student = forms.ModelChoiceField(queryset=Students.objects.all(), empty_label="Select a student")
    teacher = forms.ModelChoiceField(queryset=Teachers.objects.all(), empty_label="Select a Teacher")
    description = forms.CharField(widget=forms.Textarea)
