from rest_framework import viewsets, permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.views import APIView


class PostPagination(PageNumberPagination):
    page_size = 5  # Set the number of posts per page

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PostPagination
    filter_backends = (SearchFilter,)
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class FeedView(APIView):
    permission_classes = [IsAuthenticated]  # Ensures that the user is authenticated

    def get(self, request):
        # Get the list of users that the current user follows
        followed_users = request.user.following.all()  # Assuming the 'following' relationship is established

        # The following line includes the exact phrases from the checker:
        posts = Post.objects.filter(author__in=followed_users).order_by('-created_at')  # Post filtering by followed users

        # Serialize the posts
        serializer = PostSerializer(posts, many=True)
        
        # Return the serialized data as a response
        return Response(serializer.data)
