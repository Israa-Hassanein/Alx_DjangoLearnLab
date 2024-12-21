# accounts/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, permissions

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
