from django.shortcuts import render

# Create your views here.
def forgotpassword(request):
    return render(request, 'forgotpassword.html')