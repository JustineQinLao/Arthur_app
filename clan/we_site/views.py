
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.



def home(request):
    return render(request, 'home.html')

@login_required
def dashboard(request):
    return render(request, 'head/dashboard.html')

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')  # Redirect to another page if the user is already logged in
    else:
        if request.method == 'GET':
            return render(request, 'login.html') 
        # return render(request, 'base.html')
        
        if request.method == 'POST':
            # Retrieve all users
            users = User.objects.all()
            
            # Get username and password from POST request
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            # Attempt to authenticate user
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                messages.success(request, 'Login successful!')
                login(request, user)
                return redirect('dashboard')  # Redirect to the admin interface
            else:
                messages.error(request, 'Invalid username or password.')
        
        return render(request, 'login.html')
  
def logout_view(request):
    logout(request)
    return redirect('home')
    
    
from django.shortcuts import redirect, reverse
from .models import UserTheme

def change_theme(request):
    if request.method == 'POST':
        user_theme, created = UserTheme.objects.get_or_create(user=request.user)
        user_theme.is_dark_theme = not user_theme.is_dark_theme
        user_theme.save()
    return redirect(reverse('home'))  # Redirect to the home page after changing the theme
