from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from .models import Profile


# Registration view
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def profile(request):
    # Handle POST request to update user and profile information
    if request.method == 'POST':
        user = request.user
        
        # Update user fields like email
        user.email = request.POST['email']
        
        # Update profile fields like bio and profile picture
        if 'bio' in request.POST:
            user.profile.bio = request.POST['bio']
        
        if 'profile_picture' in request.FILES:
            user.profile.profile_picture = request.FILES['profile_picture']
        
        # Save user and profile
        user.save()
        user.profile.save()

        # Redirect to the same profile page after update
        return redirect('profile')

    # Handle GET request to render profile details
    return render(request, 'registration/profile.html', {'user': request.user})



