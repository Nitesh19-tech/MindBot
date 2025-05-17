from django.shortcuts import render, redirect
from .models import Login , Registration
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def home(request):
    return render(request, 'home.html')

def login_register_view(request):
    if request.method == 'POST':
        # Check if it's a login form or registration form
        if 'firstname' in request.POST:
            # Registration form
            first_name = request.POST.get('firstname')
            last_name = request.POST.get('lastname')
            email = request.POST.get('email')
            password = request.POST.get('password')
            username = email.split('@')[0]  # Create username from email (or customize)

            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists.")
                return redirect('login_register_view')

            if User.objects.filter(email=email).exists():
                messages.error(request, "Email already registered.")
                return redirect('login_register_view')

            user = User.objects.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password
            )
            user.save()
            messages.success(request, "Account created successfully!")
            return redirect('login_register_view')

        else:
            # Login form
            email = request.POST.get('email')
            password = request.POST.get('password')
            try:
                username = User.objects.get(email=email).username
            except User.DoesNotExist:
                messages.error(request, "Invalid email or password.")
                return redirect('login_register_view')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Login successful!")
                return redirect('home')  # change to msg page
            else:
                messages.error(request, "Invalid credentials.")
                return redirect('login_register_view')

    return render(request,'login.html')  # main template
