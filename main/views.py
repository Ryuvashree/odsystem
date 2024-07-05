# main/views.py

from django.shortcuts import render

# main/views.py
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ODApprovalForm
from .models import ODApproval
from django.conf import settings

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def courses(request):
    return render(request, 'courses.html')

def student(request):
    return render(request, 'student.html')

def admin(request):
    return render(request, 'admin.html')

def contact(request):
    return render(request, 'contact.html')

def student_view(request):
    # Your logic for the student view
    return render(request, 'student.html')

#def index(request):
    #return render(request, 'index.html')
#def form(request):
    # If there is any heavy processing, consider moving it to the background or optimizing it
    return render(request, 'form.html')

def form(request):
    return render(request, 'od_approval_form.html')

def success_page(request):
    return render(request, 'success.html')


def student_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(f'Attempting login for username: {username}')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print('user authentication successfully')
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('form')
        else:
            print('Authentication failed')
            messages.error(request, 'Invalid username or password')
    return render(request, 'student.html')
'''''
def submit_od_approval(request):
    if request.method == 'POST':
        form = ODApprovalForm(request.POST)
        if form.is_valid():
            od_approval = form.save()
            # Send email notification
            send_mail(
                'OD Approval Request Submitted',
                f"OD approval request for {od_approval.employee_name} has been submitted.",
                settings.EMAIL_HOST_USER,
                ['projectdjango2704@gmail.com'],
                fail_silently=False,
            )
            messages.success(request, 'OD approval request submitted successfully.')
            return redirect('submit_od_approval')  # Ensure 'submit_od_approval' is a valid URL name
    else:
        form = ODApprovalForm()

    return render(request, 'base.html', {'form': form})

'''

def exam(request):
    if request.method == 'POST':
        form = ODApprovalForm(request.POST)
        if form.is_valid():
            # Save form data to the database
            od_approval = form.save()

            # Construct email subject and message
            subject = f'OD Approval Form for {od_approval.student_name}'
            message = (
                f'STUDENT Name: {od_approval.student_name}\n'
                f'STUDENT ID: {od_approval.student_id}\n'
                f'Department: {od_approval.department}\n'
                f'OD Date: {od_approval.od_date}\n'
                f'Reason: {od_approval.reason}'
            )

            # Send email
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                ['projectdjango2704@gmail.com'],  # You can dynamically set the recipient email if needed
                fail_silently=False,
            )

            # Add a success message
            messages.success(request, 'Your OD approval form has been submitted successfully.')

            # Redirect to a success page
            return redirect('success_page')  # Assuming you have a success page to redirect to
        else:
            # Add an error message if the form is not valid
            messages.error(request, 'Please correct the errors below.')

    else:
        form = ODApprovalForm()

    # Render the form template
    return render(request, 'exam_form.html', {'form': form})


def exam(request):
    if request.method == 'POST':
        # Handle form submission logic here...
        
        # Redirect to success page after form submission
        return redirect('success_page')
    else:
        # Handle GET request logic here...
        pass
