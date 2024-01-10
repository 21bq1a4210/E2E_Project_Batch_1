from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import SetPasswordForm

def forgotpassword(request):

    # Check if the page is being refreshed
    if request.method == 'GET':
        print('get the command')
        if 'refreshed' in request.session:
            # Page is being refreshed
            print('Page is being refreshed')
            # step = 1
            # print(step)
            del request.session['refreshed']  # Clear the session variable
            request.session['reset_step'] = 0
        else:
            # Page is not being refreshed, set the session variable
            request.session['refreshed'] = True

    # Rest of your code...
    if request.method == 'POST':
        email = request.POST.get('email')
        user = User.objects.filter(email=email).first()
        step = 2
        if user:
            generated_otp = "123456"  # Replace this with your actual OTP generation logic
            entered_otp = request.POST.get('otp')
            print(entered_otp)
            if entered_otp == generated_otp:
                form = SetPasswordForm(user, request.POST)
                # step = 3

                if form.is_valid():
                    # Save the new password
                    form.save()
                    update_session_auth_hash(request, form.user)
                    messages.success(request, 'Password updated successfully.')

                    # Reset the step to 0 after successful password update
                    request.session['reset_step'] = 0
                    return redirect('password_reset_done')  # Use redirect to return an HttpResponse

                else:
                    messages.error(request, 'Invalid form submission. Please try again.')

                # Set the step to 3 for the password update form
                step = 3
                request.session['reset_step'] = 3
                return render(request, 'forgotpassword.html',
                              {'step': 3, 'email_exists': True, 'otp_verified': True, 'form': form})

            else:
                messages.error(request, 'Invalid OTP. Please try again.')

        else:
            messages.error(request, 'Email not found in the database.')

    # Default to Step 1
    request.session['reset_step'] = 1
    form = SetPasswordForm(user)  # Create an empty form for Step 1
    return render(request, 'forgotpassword.html',
                  {'step': 3, 'email_exists': False, 'otp_verified': False, 'form': form})
