from django.shortcuts import render, get_object_or_404
from login.views import username
from signup.models import Student, User
# Create your views here.
def dashboard(request):
    # Get the User object based on the provided 'username'
    user = get_object_or_404(User, username=username)

    # Now, retrieve the associated Student object
    student = get_object_or_404(Student, user=user)

    # Extract the required fields
    student_name = student.user.get_full_name()  # Assuming you want the full name
    roll_number = student.roll_number
    email = student.user.email
    branch = student.branch
    section = student.section
    year = student.year

    context = {
        'name': student_name,
        'rollnumber': roll_number,
        'email': email,
        'branch': branch,
        'section': section,
        'year': year,
    }

    return render(request, 'dashboard.html', context)