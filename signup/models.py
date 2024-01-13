from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

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

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll_number = models.CharField(primary_key=True, max_length=20)
    section = models.CharField(max_length=1, choices=SECTION_CHOICES)
    branch = models.CharField(max_length=3, choices=BRANCH_CHOICES)
    year = models.CharField(max_length=3, choices=YEAR_CHOICES, default='I')  # Set the default value here
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='male')  # Add the gender field

    def __str__(self):
        return self.user.username
