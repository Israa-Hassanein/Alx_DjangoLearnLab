from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, permissions
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView


class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user_to_follow = CustomUser.objects.get(id=user_id)
        if user_to_follow == request.user:
            return Response({"error": "You cannot follow yourself."}, status=400)

        request.user.following.add(user_to_follow)  # Assuming 'following' is a ManyToMany field
        return Response({"message": f"Successfully followed {user_to_follow.username}."})

class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user_to_unfollow = CustomUser.objects.get(id=user_id)
        if user_to_unfollow == request.user:
            return Response({"error": "You cannot unfollow yourself."}, status=400)

        request.user.following.remove(user_to_unfollow)
        return Response({"message": f"Successfully unfollowed {user_to_unfollow.username}."})

# Add a new view that lists all users for the authenticated user to follow/unfollow
class ListUsersView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        all_users = CustomUser.objects.all()
        user_data = [{"id": user.id, "username": user.username} for user in all_users if user != request.user]
        return Response({"users": user_data}, status=status.HTTP_200_OK)

class RegisterView(View):
    def get(self, request):
        # Handle GET request (render the registration form)
        form = UserCreationForm()
        return render(request, 'accounts/register.html', {'form': form})

    def post(self, request):
        # Handle POST request (process the submitted form)
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created successfully!')
            return redirect('login')  # Redirect to login page (adjust as needed)
        else:
            messages.error(request, 'There was an error with your submission.')
            return render(request, 'accounts/register.html', {'form': form})

class ProfileView(View):
    def get(self, request):
        # Fetch the current logged-in user’s profile
        user = request.user
        return render(request, 'accounts/profile.html', {'user': user})
    
class LoginView(View):
    def get(self, request):
        return render(request, 'accounts/login.html')

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')  # Redirect to profile page after login
            else:
                return render(request, 'accounts/login.html', {'error': 'Invalid credentials'})
        return render(request, 'accounts/login.html', {'form': form})