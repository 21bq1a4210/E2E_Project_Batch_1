# authentication/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Student

class StudentRegistrationForm(UserCreationForm):
    SECTION_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
    ]

    BRANCH_CHOICES = [
        ('CIV', 'Civil Engineering'),
        ('EEE', 'Electrical and Electronics Engineering'),
        ('MEC', 'Mechanical Engineering'),
        ('ECE', 'Electronics and Communication Engineering'),
        ('CSE', 'Computer Science Engineering'),
        ('INF', 'Information Technology'),
        ('CSM', 'Computer Science - Artificial Intelligence and Machine Learning'),
        ('CSO', 'Computer Science - Internet of Things'),
        ('CIC', 'Computer Science - Internet of Things & Cybersecurity'),
        ('AIM', 'Artificial Intelligence and Machine Learning'),
        ('AID', 'Artificial Intelligence and Data Science'),
    ]

    YEAR_CHOICES = [
        ('I', 'I'),
        ('II', 'II'),
        ('III', 'III'),
        ('IV', 'IV'),
    ]

    email = forms.EmailField(required=True)
    roll_number = forms.CharField(max_length=20, required=True)
    section = forms.ChoiceField(choices=SECTION_CHOICES, required=True)
    branch = forms.ChoiceField(choices=BRANCH_CHOICES, required=True)
    year = forms.ChoiceField(choices=YEAR_CHOICES, required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

class StudentRegistrationExtendedForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['roll_number', 'section', 'branch', 'year']
