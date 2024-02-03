# mytcapp/views.py
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import TCRequestForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from .models import TCRequest
from .forms import TCRequestForm
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.conf import settings
from .forms import CustomUserCreationForm
from django.contrib.auth import logout


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

@login_required
def home(request):
    if request.method == 'POST':
        form = TCRequestForm(request.POST)
        if form.is_valid():
            user_instance = get_user_model().objects.get(pk=request.user.pk)
            
            tc_request = form.save(commit=False)
            tc_request.user = user_instance
            tc_request.save()

            # Send email to admin
            subject = 'New TC Request Submitted'
            message = f'A new TC request has been submitted by {request.user.username}.'
            from_email = settings.DEFAULT_FROM_EMAIL
            admin_email = 'mobindasche@gmail.com'  # Replace with your admin's email
            send_mail(subject, message, from_email, [admin_email])

            messages.success(request, 'Request submitted successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Form is not valid.')
    else:
        form = TCRequestForm()

    return render(request, 'home.html', {'form': form})
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def profile(request):
    # You can retrieve the necessary user information here
    user = request.user
    context = {
        'user': user,
    }
    return render(request, 'profile.html', context)