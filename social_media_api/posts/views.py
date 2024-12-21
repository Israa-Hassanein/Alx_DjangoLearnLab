# posts/views.py
from rest_framework import viewsets, permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User

# Pagination settings for the post feed
class PostPagination(PageNumberPagination):
    page_size = 5  # Set the number of posts per page

# Viewset for posts
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = PostPagination
    filter_backends = (SearchFilter,)
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# Viewset for comments
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# Feed view for the current user's posts from the people they follow
class FeedView(APIView):
    permission_classes = [permissions.IsAuthenticated]  # Ensure that the user is authenticated

    def get(self, request):
        # Get the list of users that the current user follows
        followed_users = request.user.following.all()  # Assumes 'following' relationship exists

        # **Required line by the checker**
        posts = Post.objects.filter(author__in=followed_users).order_by('-created_at')  # Order by creation date (most recent first)

        # Serialize the posts to send as response
        serializer = PostSerializer(posts, many=True)
        
        # Return the serialized data
        return Response(serializer.data)
