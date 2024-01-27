from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from signup.models import Student, User
from signup.forms import StudentRegistrationForm, StudentRegistrationExtendedForm
from django.http import JsonResponse
# Create your views here.
def dashboard(request):
    #Get the User object based on the provided 'username'
    username = request.session.get('username', None)  # Retrieve username from session
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
   


    return render(request, 'edit.html', context)


from django.contrib import messages

@login_required
def update_profile(request):
    if request.method == 'POST':
        username = request.session.get('username', None)
        user = get_object_or_404(User, username=username)
        student = get_object_or_404(Student, user=user)

        # Update User model
        user.email = request.POST["editEmail"]
        user.save()

        # Update Student model
        #student.user.first_name = request.POST["editName"].split()[0]  # Assuming first word is the first name
        #student.user.last_name = ' '.join(request.POST["editName"].split()[1:])  # Assuming the rest is the last name
        #student.roll_number = request.POST["editRollNumber"]
        student.branch = request.POST["editBranch"]
        student.section = request.POST["editSection"]
        student.year = request.POST["editYear"]

        # Save changes to both models
        user.save()
        student.save()

        messages.success(request, 'Profile updated successfully.')
        
    return redirect('dashboard')
