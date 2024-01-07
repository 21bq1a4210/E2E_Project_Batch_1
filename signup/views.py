# authentication/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import StudentRegistrationForm, StudentRegistrationExtendedForm

def signup(request):
    if request.method == 'POST':
        user_form = StudentRegistrationForm(request.POST)
        student_form = StudentRegistrationExtendedForm(request.POST)

        if user_form.is_valid() and student_form.is_valid():
            user = user_form.save()
            student = student_form.save(commit=False)
            student.user = user
            student.save()

            # Log the user in after signing up
            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)

            messages.success(request, 'Registration success!')
            return redirect('login')
        else:
            for field, errors in user_form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")

            for field, errors in student_form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")

    else:
        user_form = StudentRegistrationForm()
        student_form = StudentRegistrationExtendedForm()

    return render(request, 'SignUp.html', {'user_form': user_form, 'student_form': student_form})
