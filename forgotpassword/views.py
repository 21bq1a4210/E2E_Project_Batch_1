from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import SetPasswordForm

def forgotpassword(request):
    step = request.session.get('reset_step', 1)

    if request.method == 'POST':
        email = request.POST.get('email')
        user = User.objects.filter(email=email).first()

        if user:
            generated_otp = "123456"  # Replace this with your actual OTP generation logic
            entered_otp = request.POST.get('otp')

            if entered_otp == generated_otp:
                if request.method == 'POST':
                    form = SetPasswordForm(user, request.POST)

                    if form.is_valid():
                        form.save()
                        update_session_auth_hash(request, form.user)
                        messages.success(request, 'Password updated successfully.')
                        # Reset the step to 1 after successful password update
                        request.session['reset_step'] = 1
                        return redirect('password_reset_done')
                    else:
                        messages.error(request, 'Invalid form submission. Please try again.')

                request.session['reset_step'] = 3
                return render(request, 'forgotpassword.html', {'step': 3, 'email_exists': True, 'otp_verified': True, 'form': form})

            else:
                messages.error(request, 'Invalid OTP. Please try again.')

        else:
            messages.error(request, 'Email not found in the database.')

    # Default to Step 1
    request.session['reset_step'] = 1
    return render(request, 'forgotpassword.html', {'step': step, 'email_exists': False, 'otp_verified': False})
